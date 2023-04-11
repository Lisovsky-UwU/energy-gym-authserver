from typing import Type
from loguru import logger

from ..orm import User
from ..orm import Token
from ..services.database import TokenDBService


class TokenController:
    def __init__(self, token_service_type: Type[TokenDBService]):
        self.service_type = token_service_type


    def generate_token(self, user: User) -> Token:
        with self.service_type() as service:
            token = service.create_for_user(user)
            service.commit()

        logger.trace(f'Сгенерирован новый токен для пользователя с ID {user.id}')
        return token
    

    def delete_token(self, token: str):
        with self.service_type() as service:
            db_token = service.get_by_token(token)
            if db_token is not None:
                service.delete(db_token)
                service.commit()
