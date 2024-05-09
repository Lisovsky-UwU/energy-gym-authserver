import io
from quart import Blueprint, request, jsonify, send_file
from loguru import logger

from ...orm import SessionCtx
from ...models import UserRole, MainServerApiMethods
from ...services import MainServerService
from ...services.database import UserDBService
from ...controllers import AuthController
from ...exceptions import AccessRightsException, InvalidRequestException, LoginError


main_server_bl = Blueprint('main_server', __name__)


@main_server_bl.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def main_server_api(path: str):
    token = request.headers.get('Authorization')
    if token is None:
        raise LoginError('Отсутствует токен в заголовке')

    with SessionCtx() as session:
        user = AuthController(
            UserDBService(session)
        ).get_user(token)

        user_id = user.id
        user_role = user.role

    try:
        method = MainServerApiMethods[path.upper().replace('-', '_').replace('/', '_')].value
    except KeyError:
        logger.warning(f'Попытка получить доступ к несуществующему методу пользователем с ID {user_id}: path = {path}')
        raise AccessRightsException('Недостаточно прав')

    
    if method.access not in UserRole[user_role.name].value:
        logger.warning(f'Попытка получить доступ к методу без достаточных прав пользователем с ID {user_id}: path = {path}')
        raise AccessRightsException('Недостаточно прав')

    if method.needjson and request.headers.get('Content-Type') != 'application/json':
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')
    
    response = await MainServerService().send_request(
        method   = request.method,
        endpoint = method.endpoint,
        user_id  = user_id,
        body     = (await request.get_json()),
    )

    if isinstance(response, (dict, list)):
        return jsonify(response)
    else:
        return await send_file(io.BytesIO(response), attachment_filename='result.xlsx')
