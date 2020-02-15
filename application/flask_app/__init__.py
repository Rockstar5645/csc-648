
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.config import db_conn, track_mods
import sqlalchemy.dialects.mysql.pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretSquirrel'
app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_mods
db = SQLAlchemy(app)

from flask_app import routes
