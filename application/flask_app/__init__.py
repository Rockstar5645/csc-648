from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['AQLALCHEMY_DATABASE_URI'] = 'mysql://test@localhost/db_six'
db = SQLAlchemy(app)

from flask_app import routes