from src.app_pkg import db
from src.app_pkg.routes.common import validate_helper






class User(object):

    user_id = 0
    session_token = ""
    username = 'default'
    email = ''
    isloggedin = False

    def __init__(self, cookies):
        if 'token' in cookies:
            self.session_token = cookies['token']
        if validate_helper(self.session_token) == True:
            self.isloggedin = True
            self.user_id = db.get_user_id(self.session_token)
            self.fill_user_data()

    def fill_user_data(self):
        data = db.get_user_data(self.user_id)
        if len(data) > 0:
            self.username = data[0][5]
            self.email = data[0][3]

    def get_messages(self):
        return db.get_all_messages(self.session_token)

    def get_digital_media(self):
        return db.get_user_digital_media(self.user_id)
        