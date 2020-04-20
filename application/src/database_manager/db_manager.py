from src.database_manager import database_connection
from src.database_manager.register import register
from src.database_manager.login import login

from src.database_manager.upload import upload

from src.database_manager.validate_session import validate_session

from src.config import redis_conn
import redis
import sys


##############################################
#         DATABASE OBJECT DEFINITION         #
##############################################
# database object defined here.
#
# owns: mysql connection object (conn, cursor)
#
# provides: constructor, destructor, and 
#     various query helper functions


class DB:

    def __init__(self):
        self.db_connection = database_connection.MyDB()

        try:
            self.redis_connection = redis.Redis(**redis_conn)
        except redis.ConnectionError as err:
            print("ERROR, UNABLE TO CONNECT TO REDIS: {}\n\n".format(err))
            raise

    def register(self, username, email, password):
        return register(username, email, password, self.db_connection, self.redis_connection)

    def login(self, username,  password, ip_address):
        return login(username, password, ip_address, self.db_connection, self.redis_connection)

    def validate_session(self, session_token):
        return validate_session(session_token, self.redis_connection)

    # added upload to test db query for uploads
    def upload(self, filename, description, price, category):
        return upload(filename, description, price, category, self.db_connection, self.redis_connection)


    def search(self, term, category):
        if term =='': # if search term was blank
            return self.get_category(category)
        else: # search like for term
            return self.search_like(term, category)

    def search_like(self, term, category):
        if category == 'all':
            # check all categories for search term
            self.db_connection.query(
                "SELECT * "
                "FROM digital_media_test "
                "WHERE `name` LIKE %s OR `description` LIKE %s",
                ("%" + term + "%","%" + term + "%",)
            )
        else:
            # check only for matches in certain category
            self.db_connection.query(
                "SELECT * "
                "FROM digital_media_test "
                "WHERE (`name` LIKE %s OR `description` LIKE %s) AND category LIKE %s",
                ("%" + term + "%","%" + term + "%", "%" + category,)
            )
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        # if result is empty, get all objects in category
        if len(data) == 0:
            data = self.get_category(category)
        return data

    def get_category(self, category):
        # get all rows of a certain category
        self.db_connection.query("SELECT * FROM digital_media_test WHERE category LIKE %s", ("%" + category + "%",))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        # if category is empty, return all rows in table
        if len(data) == 0:
            data = self.get_all_media()
        return data
    
    def get_all_media(self):
        # return all rows in table
        self.db_connection.query("SELECT * FROM digital_media_test")
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data

    def get_category_select_field(self):
        # this returns the categories for a select field in a form
        self.db_connection.query("SELECT * FROM categories")
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        # make a usable list of tuples for select field
        cats = [(c[1], c[1]) for c in data]
        return cats

    def get_team(self, name=None):
        if name == None: # if no param : return whole team table
            self.db_connection.query("SELECT * FROM team_about")
        else: # get team_member
            self.db_connection.query("SELECT * FROM team_about WHERE `name` LIKE %s", ("%" + name + "%",))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data
