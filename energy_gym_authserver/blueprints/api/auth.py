import json
from typing import List
from quart import Blueprint, request
from loguru import logger

from ...orm import SessionCtx, User
from ...services.database import UserDBService
from ...controllers import AuthController
from ...models import UserRole
from ...exceptions import InvalidRequestException, RegistrationError, LoginError
from ...utils import generate_hid
from ...configmodule import config


auth_bl = Blueprint('auth', __name__)

_student_cards_list: List[int] = None


def student_card_check_exists(student_card: str):
    global _student_cards_list
    if _student_cards_list is None:
        _student_cards_list = list(map(str, json.load(open(config.common.student_cards_file))))
    
    return student_card in _student_cards_list


@auth_bl.post('/check-studcard')
async def check_studcard():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')
    
    student_card = str(data.get('studentCard'))
    
    if len(student_card) != 8 and len(student_card) != 7:
        raise InvalidRequestException('Длина студенческого билета должна быть 7-8 символов')
    if not student_card.isdigit():
        raise InvalidRequestException('Студенческий билет должен быть числом')
    if not student_card_check_exists(student_card):
        raise InvalidRequestException('Номер студенческого не найден')
    
    with SessionCtx() as session:
        user_serivce = UserDBService(session)
        return {
            'alreadyExists': user_serivce.get_by_student_card( int(data.get('studentCard')) ) is not None
        }   


@auth_bl.post('/signup')
async def signup():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    with SessionCtx() as session:
        user_service = UserDBService(session)

        if user_service.get_by_student_card(data['studentCard']):
            raise RegistrationError('Данный номер студенческого уже зарегистрирован')

        if len(data['password']) < 8:
            raise RegistrationError('Пароль должен быть не меньше 8 символов')

        student_card = str(data.get('studentCard'))
    
        # Студенческие билеты вроде как должны быть по 8 символов, однако при экспорте тестовых данных
        # с реальных студаков был один на 7 символов. Может это кривой экспорт и потеряли цифру просто,
        # но условие сделать надо
        if len(student_card) != 8 and len(student_card) != 7:
            raise InvalidRequestException('Длина студенческого билета должна быть 7-8 символов')
        if not student_card.isdigit():
            raise InvalidRequestException('Студенческий билет должен быть числом')
        if not student_card_check_exists(student_card):
            raise InvalidRequestException('Номер студенческого не найден')

        user = user_service.create(
            User(
                student_card = int(data['studentCard']),
                firstname    = data['firstname'],
                secondname   = data['secondname'],
                surname      = data['surname'],
                group        = data['group'],
                hid          = generate_hid(data['studentCard'], data['password']),
                role         = UserRole.STUDENT,
            )
        )
        user_service.commit()
        logger.info(f'Зарегистрирован новый пользователь: {user.to_dict(get_id = True)}')

        return {
            'token': AuthController(user_service).generate_token(user.id),
            'userData': user.to_dict()
        }


async def do_login(data, user_role: UserRole) -> dict:
    with SessionCtx() as session:
        user_service = UserDBService(session)

        user = user_service.get_by_student_card(data.get('login'), user_role)
        if user is None:
            raise LoginError('Неверный логин или пароль')
        
        if user.hid != generate_hid(data['login'], data['password']):
            raise LoginError('Неверный логин или пароль')

        logger.debug(f'Авторизация студента id={user.id}')
        return {
            'token': AuthController(user_service).generate_token(user.id),
            'userData': user.to_dict()
        }


@auth_bl.post('/login')
async def login():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    return await do_login(data, UserRole.STUDENT)


@auth_bl.post('/login/coach')
async def login_coach():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    return await do_login(data, UserRole.COACH)


@auth_bl.post('/login/admin')
async def login_admin():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    return await do_login(data, UserRole.ADMIN)


@auth_bl.get('/check-login')
async def check_login():
    token = request.headers.get('Authorization')
    if token is None:
        raise LoginError('Отсутствует токен в заголовке запроса')

    with SessionCtx() as session:
        user = AuthController(UserDBService(session)).get_user(token)
        return user.to_dict()
