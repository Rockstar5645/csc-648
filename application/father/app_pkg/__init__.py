from flask import Flask
from father.database_manager.db_manager import DB
from father.config import flags

# init flask application
app = Flask(__name__)
# create DB object
db = DB()

if '-p' in flags:
    from father.app_pkg.routing import routing_prod

if '-d' in flags:
    from father.app_pkg.routing import routing_dev
