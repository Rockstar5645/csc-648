from flask import Flask
from father.database_manager.db_manager import DB
# init flask application
app = Flask(__name__)
# create DB object
db = DB()

from father.app_pkg import routing
