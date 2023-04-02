from typing import Type

from .controllers import UserControleer
from .controllers import TokenController
from .services.database import UserDBService
from .services.database import TokenDBService


class ControllerFabric:

    user_db_service_type: Type[UserDBService]
    token_db_service_type: Type[TokenDBService]


    @classmethod
    def user_controller(cls) -> UserControleer:
        return UserControleer(cls.user_db_service_type)


    @classmethod
    def token_controller(cls) -> TokenController:
        return TokenController(cls.token_db_service_type)
