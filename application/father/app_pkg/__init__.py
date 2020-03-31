from flask import Flask

# init flask application
app = Flask(__name__)
# create DB object
from father.app_pkg.db_obj import db

from father.app_pkg import routing