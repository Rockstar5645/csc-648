from src.database_manager import database_connection
from src.database_manager.register import register
from src.database_manager.login import login
from src.database_manager.logout import logout
from src.database_manager.get_session_id import get_session_id
from src.database_manager.send_message import send_message
from src.database_manager.get_all_messages import get_all_messages
from src.database_manager.get_message_by_id import get_message_by_id
from src.database_manager.upload_file import upload_file
from src.database_manager.delete_file import delete_file
from src.database_manager.validate_session import validate_session
from src.database_manager.search import search
from src.database_manager.select_fields import get_media_type_select_field, get_category_select_field
from src.database_manager.team import get_team
from src.database_manager.helpers import get_media_type, get_category_type
from src.database_manager.user_functions import get_user_data
from src.database_manager.get_user_digital_media import get_user_digital_media
from src.database_manager.get_media_path import get_digital_media_path_by_id

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

    def login(self, username,  password, ip_address='127.0.0.1'):
        return login(username, password, ip_address, self.db_connection, self.redis_connection)

    def validate_session(self, session_token):
        return validate_session(session_token, self.redis_connection)

    def logout(self, session_token):
        return logout(session_token, self.redis_connection)

    def send_message(self, session_token, media_id, subject, message_body): 
        session_status = get_session_id(session_token, self.redis_connection)
        if session_status['status'] != 'success':
            return session_status
        else:
            return send_message(session_status['user_id'], media_id, subject, message_body, self.db_connection)

    def get_all_messages(self, session_token):
        session_status = get_session_id(session_token, self.redis_connection)
        if session_status['status'] != 'success':
            return session_status
        else:
            return get_all_messages(session_status['user_id'], self.db_connection)

    def get_message_by_id(self, session_token, message_id):
        session_status = get_session_id(session_token, self.redis_connection)
        if session_status['status'] != 'success':
            return session_status
        else:
            return get_message_by_id(message_id, session_status['user_id'], self.db_connection)

    def upload_file(self, owner, filename, description, file_path, thumb_path, category, media_type, price, session_token):
        return upload_file(owner, filename, description, file_path, thumb_path, category, media_type, price, session_token, self.db_connection)

    def delete_file(self):
        return delete_file()

    def search(self, params):
        return search(self.db_connection, params)
    
    def get_media_type_select_field(self):
        return get_media_type_select_field(self.db_connection)

    def get_category_select_field(self):
        return get_category_select_field(self.db_connection)

    def get_team(self, name=None):
        return get_team(self.db_connection, name)

    def get_media_type(self, id):
        return get_media_type(self.db_connection, id)
    
    def get_category_type(self, id):
        return get_category_type(self.db_connection, id)

    def get_user_id(self, session_token):
        session_status = get_session_id(session_token, self.redis_connection)
        if session_status['status'] == 'success':
            return session_status['user_id']

    def get_user_data(self, user_id):
        return get_user_data(user_id, self.db_connection)

    def get_user_digital_media(self, user_id):
        return get_user_digital_media(user_id, self.db_connection)

    def get_digital_media_path_by_id(self, id):
        return get_digital_media_path_by_id(id, self.db_connection)

