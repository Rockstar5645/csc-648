from src.database_manager.authenticate_user import authenticate_user
from src.database_manager.db_manager import DB
from datetime import datetime 
from src.database_manager.send_message import send_message

rightnow = datetime.now()

print(rightnow)

db = DB().db_connection
#abc = db.login('apples', 'apples')
#token = abc['token']

return_val = send_message(2, 2, 'hey I wanna buy your thin', 'how much does it cost', db)
print(return_val)

"""
sender_id = 2
media_id = 1
subject = 'hey I wanna buy your thin'
message_body = 'how much does it cost'

get_owner_id_query = ("SELECT owner_id FROM digital_media WHERE media_id=%s")
db.query(get_owner_id_query, (1,))

for recipient_id in db.fetchall()[0]:
    add_message = ("INSERT INTO messages "
                    "(time_stamp, sender, recipient, message_content, media_id, seen, subject) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    print(recipient_id)
    print(sender_id)
    time_stamp = datetime.now()

    values_to_be_inserted = (time_stamp, sender_id, recipient_id, message_body, media_id, False, subject)

    db.query(add_message, values_to_be_inserted)
    db.commit()
"""