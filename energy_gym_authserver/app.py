from quart import Quart
from quart_cors import cors

from .configmodule import config
# from .blueprints import api_bl


def build_app() -> Quart:
    app = Quart(__name__)

    # app.register_blueprint(api_bl, url_prefix='/api/v1')

    if config.common.use_dev:
        cors(app, allow_origin='*')

    return app
