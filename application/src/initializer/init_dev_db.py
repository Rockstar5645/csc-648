from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import *
from src.initializer.aux2_methods import *

db = MyDB()

print('Initializing Database skeleton: creating tables')
initialize_database_skeleton(db)

print('Inserting test data to initialize development environment')
fill_team_about(db)
fill_media_types(db)

create_test_users(db)

# create an initial default category, for the digital media entries to reference
print('Creating default category for digital media entries to reference')
db.query("INSERT INTO categories (category) VALUES (%s)", ('art',))
db.commit()
print('default category created')

fill_digital_media(db)

simulate_test_messages(db)

print('Development database initialization sequence successfully completed.')