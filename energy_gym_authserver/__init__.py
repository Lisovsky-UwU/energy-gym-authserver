from .log import init_logger
from .app import build_app
from .app import run_app
from .fabrics import ControllerFabric
from .services.database import UserDBService
from .services.database import TokenDBService


def start():
    init_logger()
    try:
        ControllerFabric.user_db_service_type = UserDBService
        ControllerFabric.token_db_service_type = TokenDBService

        run_app(
            build_app(
                UserDBService,
                TokenDBService
            )
        )
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    start()
