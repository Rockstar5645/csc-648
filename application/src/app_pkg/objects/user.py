


class User(object):

    def __init__(self):
        self.valid = 'invalid'
        self.user_id = None
        self.session_token = None
        self.client = None

    def login(self, user_id, session_token, client):
        self.valid = 'valid'
        self.user_id = user_id
        self.session_token = session_token
        self.client = client

    def __str__(self):
        return self.valid