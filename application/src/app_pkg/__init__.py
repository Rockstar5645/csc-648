########################################
#   Flask Applciation
######################################

from flask import Flask
from src.database_manager.db_manager import DB
from os.path import join, dirname, realpath

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/')

# init flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'DEADBEEF'


app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

# recaptcha junk here
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY']= '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}

# create DB object
db = DB()

# import routes
from src.app_pkg.routes import search, about, login, registration, logout, download
from src.app_pkg.routes import user_profile, submit_media, message


