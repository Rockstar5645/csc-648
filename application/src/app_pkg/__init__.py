from flask import Flask
from src.database_manager.db_manager import DB
from src.config import flags

# init flask application
app = Flask(__name__)
# create DB object
db = DB()

if '-p' in flags:
    from src.app_pkg.routing import routing_prod

if '-d' in flags:
    from src.app_pkg.routing import routing_dev
