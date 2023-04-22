import os
from flask import Blueprint


webgui = Blueprint('webgui', 'webgui', static_folder=os.path.join(os.getcwd(), "static"))


from . import routes
