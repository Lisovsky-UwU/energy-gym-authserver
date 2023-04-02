import quart.flask_patch # must be first import if we use flask extensions

from typing import Type
from quart import Quart
from quart import Request
from quart_cors import cors
from flask_login import LoginManager # use it becouse quart_login is broke

from .configmodule import config
from .blueprints import api_bl
from .exceptions import LoginError
from .services.database import UserDBService
from .services.database import TokenDBService


def build_app(user_service_type: Type[UserDBService], token_service_type: Type[TokenDBService]) -> Quart:
    app = Quart(__name__)

    app.secret_key = config.common.secret_key

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        with user_service_type() as service:
            return service.get_by_id(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        raise LoginError('Ошибка доступа: требуется авторизация')
    
    @login_manager.request_loader
    def request_loader(request: Request):
        token = request.headers.get('Token')
        if token is not None:
            with token_service_type() as service:
                db_token = service.get_by_token(token)

                if db_token is not None:
                    return db_token.users

        return None

    app.register_blueprint(api_bl, url_prefix='/api/v1')

    if config.common.use_dev:
        cors(app, allow_origin='*')

    return app
