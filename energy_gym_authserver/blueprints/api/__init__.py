from quart import Blueprint


api = Blueprint('api', 'api')


from .auth import auth_bl
from .main_server import main_server_bl

api.register_blueprint(auth_bl, url_prefix='/auth')
api.register_blueprint(main_server_bl)


from . import handlers
