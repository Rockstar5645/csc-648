import bcrypt
import base64
import hashlib
from src.database_manager.generate_session import generate_session
import mysql.connector

def upload_file(owner, filename, description, file_path, thumb_path, category, media_type, price, session_token, db):
    add_digital_media = ("INSERT INTO digital_media  "
                               "(owner_id, name, description, file_path, thumbnail_path, category, media_type, price, approval) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    # added owner_id = 1 for testing
    values = (owner, filename, description, file_path, thumb_path, category, media_type, price, 0)
    db.query(add_digital_media, values)
    db.commit()

