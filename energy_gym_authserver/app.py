import asyncio
from quart import Quart
from loguru import logger
from hypercorn import Config
from hypercorn.asyncio import serve
from quart_cors import cors

from .configmodule import config
from .blueprints import api_bl, webgui_bl
from .services.database import UserDBService


def build_app() -> Quart:
    logger.info('Сборка приложения')
    app = Quart(__name__)

    app.secret_key = config.common.secret_key

    logger.info('Настройка модуля авторизации')

    logger.info('Регистрация шаблонов')
    app.register_blueprint(api_bl, url_prefix='/api/v1')
    app.register_blueprint(webgui_bl)

    if config.common.use_dev:
        logger.debug('Используется окружение разработки')
        cors(app, allow_origin='*')

    return app


def run_app(app: Quart):
    logger.info('Запуск сервера')
    app_config = Config()
    app_config.bind = config.local_server.address
    asyncio.run(serve(app, config=app_config))
