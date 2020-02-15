from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.config import db_addr, track_mods

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_addr
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_mods
db = SQLAlchemy(app)

from flask_app import routes