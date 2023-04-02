from quart import Blueprint
from quart import request
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from ...fabrics import ControllerFabric
from ...exceptions import InvalidRequestException


auth_bl = Blueprint('auth', 'auth')


@auth_bl.post('/signup')
async def signup():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    user = ControllerFabric.user_controller().registrate_user(**data)

    login_user(user, remember = True if data.get('remember') else False)

    return { 'token': ControllerFabric.token_controller().generate_token(user).token }


@auth_bl.post('/login')
async def login():
    data = await request.get_json()
    if data is None:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')

    user = ControllerFabric.user_controller().login_user(
        student_card = data['student_card'],
        password     = data['password']
    )

    login_user(user, remember=True if data.get('remember') else False)

    return { 'token': ControllerFabric.token_controller().generate_token(user).token }


@auth_bl.get('/check-login')
@login_required
async def check_login():
    return current_user.to_dict()


@auth_bl.get('/logout')
@login_required
async def logout():
    token = request.headers.get('Token')
    if token is not None:
        ControllerFabric.token_controller().delete_token(token)

    return { 'result': logout_user() }
