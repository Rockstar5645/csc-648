from flask import Flask
from src.database_manager.db_manager import DB

# init flask application
app = Flask(__name__)

# create DB object
db = DB()
#moment = Moment(app)

from src.app_pkg import routes


