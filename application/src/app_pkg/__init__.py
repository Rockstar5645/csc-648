from flask import Flask
from src.database_manager.db_manager import DB
from flask_login import (LoginManager, login_user, 
                         current_user, logout_user)
from itsdangerous import URLSafeTimedSerializer

# init flask application
app = Flask(__name__)

# create DB object
db = DB()
#moment = Moment(app)

#Flask-Login Login Manager
login_manager = LoginManager()
#Tell the login manager where to redirect users to display the login page
login_manager.login_view = "/login"
#Setup the login manager. 
login_manager.setup_app(app) 
from src.database_manager.objects import user

# import routes
from src.app_pkg import routes


