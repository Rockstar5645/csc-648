from src.app_pkg import login_manager
from flask_login import UserMixin


class User(UserMixin):
    """
    User Class for flask-Login
    """
    def __init__(self, userid, password):
        self.id = userid
        self.password = password

    def get_auth_token(self):
        """
        Encode a secure token for cookie
        """
        data = [str(self.id), self.password]
        return data

    @staticmethod
    def get(userid):
        """
        Static method to search the database and see if userid exists.  If it 
        does exist then return a User Object.  If not then return None as 
        required by Flask-Login. 
        """
        #For this example the USERS database is a list consisting of 
        #(user,hased_password) of users.
        pass

@login_manager.user_loader
def load_user(userid):
    """
    Flask-Login user_loader callback.
    The user_loader function asks this function to get a User Object or return 
    None based on the userid.
    The userid was stored in the session environment by Flask-Login.  
    user_loader stores the returned User object in current_user during every 
    flask request. 
    """
    return User.get(userid)