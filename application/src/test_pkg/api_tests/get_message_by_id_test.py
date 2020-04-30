from src.database_manager.database_connection import MyDB
from src.database_manager.get_message_by_id import get_message_by_id

db = MyDB()

msg = get_message_by_id(11, 5, db)

print()
