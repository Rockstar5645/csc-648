########################################
#   Flask Applciation
######################################

from flask import Flask
from src.database_manager.db_manager import DB

# init flask application
app = Flask(__name__)

# recaptcha junk here
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}

# create DB object
db = DB()

# import routes
from src.app_pkg import routes


