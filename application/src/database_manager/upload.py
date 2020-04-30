import bcrypt
import base64
import hashlib
from src.database_manager.generate_session import generate_session
import mysql.connector

def upload(filename, description, file_path, thumb_path, category, media_type, price, session_token, db):
    add_digital_media = ("INSERT INTO digital_media  "
                               "(owner_id, name, description, file_path, thumbnail_path, category_id, media_type_id, price, approval) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    # added owner_id = 1 for testing
    values = (1, filename, description, file_path, thumb_path, category, media_type, price, 0)
    db.query(add_digital_media, values)
    db.commit()

