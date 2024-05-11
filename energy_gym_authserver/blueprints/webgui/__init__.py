import os
from quart import Blueprint


webgui = Blueprint('webgui', __name__, static_folder=os.path.join(os.getcwd(), "static"))


from . import routes
