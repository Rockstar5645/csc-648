from src.app_pkg import db
from src.app_pkg.routes.common import validate_helper






class User(object):

    user_id = 0
    username = 'default'
    email = ''
    isloggedin = False

    def __init__(self, cookies):
        session_token = 'None'
        if 'token' in cookies:
            session_token = cookies['token']
        if validate_helper(session_token) == True:
            self.isloggedin = True
            self.user_id = db.get_user_id(session_token)
            self.fill_user_data()

    def fill_user_data(self):
        data = db.get_user_data(self.user_id)
        self.username = data[0][5]
        self.email = data[0][3]
        