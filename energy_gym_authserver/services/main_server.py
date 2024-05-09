import aiohttp
from typing import Optional
from typing import Dict
from loguru import logger

from ..configmodule import config
from ..exceptions import MainServerRequestException


class MainServerService:

    def __init__(self, timeout: int = 30):
        self.timeout = timeout


    @property
    def timeout_aiohttp(self) -> aiohttp.ClientTimeout:
        return aiohttp.ClientTimeout(total=self.timeout)


    async def send_request(
        self, 
        method: str, 
        endpoint: str, 
        user_id: int = None,
        body: Optional[Dict] = None,
        headers: Optional[Dict] = {},
    ):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout_aiohttp) as session:
                logger.debug(f'Запрос пользователя с ID {user_id} к главному серверу {method} {endpoint}: {body}')
                headers['Token'] = config.main_server.token
                headers['user-id'] = str(user_id)
                async with session.request(
                    method  = method,
                    url     = config.main_server.formated_base_url + endpoint,
                    json    = body,
                    headers = headers,
                ) as resp:
                    if resp.status == 405:
                        raise MainServerRequestException('Метод не поддерживается', status_code=405)
                    
                    if resp.content_type == 'application/json':
                        resp_text = await resp.json()
                        if resp.status == 200:
                            return resp_text['data']
                        else:
                            raise MainServerRequestException(resp_text['error_message'], status_code=resp.status)
                    else:
                        return await resp.read()
        
        except aiohttp.ClientConnectionError:
            raise MainServerRequestException('Ошибка подключения к главному серверу')
