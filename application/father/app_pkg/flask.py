


class FLASK(object):

    def __init__(self):
        # init flask application
        self.app = Flask(__name__)
        # create DB object
        self.db = DB()