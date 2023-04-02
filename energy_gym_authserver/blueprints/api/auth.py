from quart import Blueprint
from quart import request
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from ...exceptions import LoginError
from ...exceptions import InvalidRequestException
from ...services.database import UserDBService
from ...services.database import TokenDBService


auth_bl = Blueprint('auth', 'auth')


@auth_bl.post('/sing-up')
async def sing_up():
    return { 'result': 'sing-up' }


@auth_bl.post('/login')
async def login():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    with UserDBService() as service:
        user = service.get_by_student_card(data['student_card'])
    
    if user is None or user.password != data['password']:
        raise LoginError('Неверный логин или пароль')
    
    with TokenDBService() as service:
        token = service.create_for_user(user)
        service.commit()

    login_user(user, remember=True if data['remember'] else False)

    return { 'token': token.token }


@auth_bl.get('/check-login')
@login_required
async def check_login():
    return current_user.to_dict()


@auth_bl.get('/logout')
@login_required
async def logout():
    token = request.headers.get('Token')
    if token is not None:
        with TokenDBService() as service:
            db_token = service.get_by_token(token)
            if db_token is not None:
                service.delete(db_token)
                service.commit()

    return { 'result': logout_user() }
