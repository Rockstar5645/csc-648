import bcrypt
import base64
import hashlib
from src.database_manager.generate_session import generate_session
import mysql.connector

def upload(filename, description, file_path, thumb_path, category, price, session_token, db):
    add_digital_media = ("INSERT INTO digital_media  "
                               "(name, description, file_path, thumbnail, category, price, approval) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    values = (filename, description, file_path, thumb_path, category, price, 0)
    db.query(add_digital_media, values)
    db.commit()

