from src.database_manager.database_connection import MyDB
from src.database_manager.get_all_messages import get_all_messages

db = MyDB()

vals = get_all_messages(1, db)

print(vals['message-list'][0]['time_stamp'])

print(vals)