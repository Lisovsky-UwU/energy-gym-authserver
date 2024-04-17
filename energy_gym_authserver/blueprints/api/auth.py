from quart import Blueprint, request
from loguru import logger

from ...orm import SessionCtx, User
from ...services.database import UserDBService
from ...controllers import AuthController
from ...models import UserRole
from ...exceptions import InvalidRequestException, RegistrationError, LoginError
from ...utils import generate_hid


auth_bl = Blueprint('auth', __name__)


@auth_bl.post('/signup')
async def signup():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    with SessionCtx() as session:
        user_service = UserDBService(session)

        if user_service.get_by_student_card(data['studentCard']):
                raise RegistrationError('Данный номер студенческого уже зарегистрирован')

        user = user_service.create(
            User(
                student_card = data['studentCard'],
                firstname    = data['firstname'],
                secondname   = data['secondname'],
                surname      = data['surname'],
                group        = data['group'],
                hid          = generate_hid(data['studentCard'], data['password']),
                role         = UserRole.STUDENT.name,
            )
        )
        user_service.commit()
        logger.info(f'Зарегистрирован новый пользователь: {user.to_dict(get_id = True)}')

        return {
            'token': AuthController(user_service).generate_token(user.id),
            'userData': user.to_dict()
        }


@auth_bl.post('/login')
async def login():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    with SessionCtx() as session:
        user_service = UserDBService(session)

        user = user_service.get_by_student_card(data.get('login'))
        if user is None:
            raise LoginError('Неверный логин или пароль')
        
        if user.hid != generate_hid(data['login'], data['password']):
            raise LoginError('Неверный логин или пароль')

        logger.debug(f'Авторизация пользователя id={user.id}')
        return {
            'token': AuthController(user_service).generate_token(user.id),
            'userData': user.to_dict()
        }


@auth_bl.get('/check-login')
async def check_login():
    token = request.headers.get('Authorization')
    if token is None:
        raise LoginError('Отсутствует токен в заголовке запроса')

    with SessionCtx() as session:
        user = AuthController(UserDBService(session)).get_user(token)
        return user.to_dict()
