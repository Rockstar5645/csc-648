
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.db.db_manager import DB_Manager
from flask_app.db.config import db_conn, track_mods
import sqlalchemy.dialects.mysql.pymysql
import os

# this is for relative accessing files with only a relative path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
db_manager = DB_Manager()
db_manager.init_db()

from flask_app import routes
