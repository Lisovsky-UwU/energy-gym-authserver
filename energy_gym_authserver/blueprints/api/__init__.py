from quart import Blueprint


api = Blueprint('api', 'api')


from .auth import auth_bl

api.register_blueprint(auth_bl, url_prefix='/auth')


from . import handlers
