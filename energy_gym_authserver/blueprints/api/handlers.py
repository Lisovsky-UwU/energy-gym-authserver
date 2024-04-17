import json
import quart
from loguru import logger

from . import api
from ...exceptions import InvalidRequestException
from ...exceptions import EnergyGymAuthServerException


@api.after_request
async def response_format(response: quart.Response):
    body = await response.get_json()
    if isinstance(body, dict):
        logger.debug(f'{quart.request.remote_addr} [{quart.request.method}] {quart.request.path} <- ({response.status_code}) {body}')
    else:
        logger.debug(f'{quart.request.remote_addr} [{quart.request.method}] {quart.request.path} <- ({response.status_code}) Not json data')

    if not (isinstance(body, dict) and body.get('error', False)):
        response.data = json.dumps({'error': False, 'data': body})

    return response


@api.before_request
async def json_chek():
    logger.debug(f'{quart.request.remote_addr} [{quart.request.method}] {quart.request.path} -> {await quart.request.data}')
    if await quart.request.get_json() and not quart.request.is_json:
        raise InvalidRequestException('Тело запроса должно быть в формате JSON')


@api.errorhandler(Exception)
async def error_handle(error: Exception) -> quart.Response:
    if not isinstance(error, EnergyGymAuthServerException):
        logger.exception(f'Непредвиденная ошибка', error)

    response = {
        'error': True,
        'error_type': type(error).__name__,
        'error_message': str(error)
    }
    
    return response, error.status_code if hasattr(error, 'status_code') else 500 # type: ignore
