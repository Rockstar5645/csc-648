


class User(object):

    def __init__(self):
        self.user_id = None
        self.session_token = None

    def login(self, user_id, session_token):
        self.user_id = user_id
        self.session_token = session_token