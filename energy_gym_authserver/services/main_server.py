import aiohttp
from typing import Optional
from typing import Dict
from loguru import logger

from ..configmodule import config
from ..exceptions import MainServerRequestException
from ..models import MainServerApiMethods


class MainServerService:
    
    async def send_request(self, method: MainServerApiMethods, body: Optional[Dict] = None):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout_aiohttp) as session:
                logger.info(f'Запрос к главному серверу {method}: {body}')
                async with session.request(
                    method  = method.value['method'],
                    url     = config.main_server.formated_base_url + method.value['endpoint'],
                    json    = body,
                    headers = { 'Token': config.main_server.token }
                ) as resp:
                    resp_text = await resp.json()
                    if resp_text['error']:
                        raise MainServerRequestException(resp_text['error_message'])
                    else:
                        return resp_text['data']
        
        except aiohttp.ClientError:
            raise MainServerApiMethods('Ошибка подключения к серверу')
