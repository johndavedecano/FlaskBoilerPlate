from flask import Flask
import jinja2
from models import db

# IMPORT BLUEPRINTS
from controllers.BaseController import BaseController
from controllers.errors import errors

from config import *

# APPLICATION INITIALIZATION AND CONFIGS
app = Flask(__name__, static_folder=ASSETS_FOLDER, template_folder=TEMPLATE_FOLDER)

# GET CONFIGURATION FROM config.py
app.config.from_object('config')

# DB INIT
db.init_app(app)
db.app = app

# SET JINJA TEMPLATE PATHS FROM config.py
app.jinja_loader = JINJA_ENVIRONMENT

# REGISTER CONTROLLERS HERE
app.register_blueprint(BaseController)
app.register_blueprint(errors)
# BOOT APPLICATION
if __name__ == '__main__':
    app.run()
