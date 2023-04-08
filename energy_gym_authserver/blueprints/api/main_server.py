from quart import Blueprint
from quart import request
from quart import jsonify
from flask_login import login_required
from flask_login import current_user

from ...models import UserRole
from ...models import MainServerApiMethods
from ...services import MainServerService
from ...exceptions import AccessRightsException
from ...exceptions import InvalidRequestException


main_server_bl = Blueprint('main_server', 'main_server')


@main_server_bl.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
async def main_server_api(path: str):
    try:
        method = MainServerApiMethods[path.upper().replace('-', '_').replace('/', '_')].value
    except KeyError:
        raise AccessRightsException('Недостаточно прав')
    
    if method.access not in UserRole[current_user.role].value:
        raise AccessRightsException('Недостаточно прав')

    if method.needjson and request.headers.get('Content-Type') != 'application/json':
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')
    
    return jsonify(
        await MainServerService().send_request(
            method   = request.method,
            endpoint = method.endpoint,
            body     = (await request.get_json()),
            headers  = { 'user-id': str(current_user.id) },
        )
    )
