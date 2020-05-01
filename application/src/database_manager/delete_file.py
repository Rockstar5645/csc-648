from src.database_manager.generate_session import generate_session
import mysql.connector

def delete_file():
    delete_digital_media = ("DELETE FROM digital_media WHERE ...")
    db.query(delete_digital_media)
    db.commit()