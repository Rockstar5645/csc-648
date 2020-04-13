from flask import Flask
from src.database_manager.db_manager import DB
from flask_login import (LoginManager, login_required, login_user, 
                         current_user, logout_user)
from itsdangerous import URLSafeTimedSerializer

# init flask application
app = Flask(__name__)

# create DB object
db = DB()
#moment = Moment(app)

#Flask-Login Login Manager
login_manager = LoginManager()

from src.app_pkg import routes


