import bcrypt
import base64
import hashlib
from src.database_manager.generate_session import generate_session
import mysql.connector

def upload(self):
    # TODO: implement upload(), query, commit, and return, check params
    data = self.db_connection.fetchall()
    self.db_connection.query("SELECT * FROM digital_media_test...")
    self.db_connection.commit()
    return data
