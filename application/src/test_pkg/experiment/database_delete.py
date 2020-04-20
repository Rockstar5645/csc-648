from src.database_manager import database_connection
from src.config import db_conn
import mysql.connector
import pytest

db_conn['user'] = 'roots'

try:
    db = database_connection.MyDB(db_conn)
except mysql.connector.Error as err:
    pass