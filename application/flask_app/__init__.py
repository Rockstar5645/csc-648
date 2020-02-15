from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db_addr

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_addr
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_app import routes