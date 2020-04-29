from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import *
from src.initializer.aux2_methods import *
from src.initializer.auxil_3 import *

db = MyDB()

print('Initializing Database skeleton: creating tables')
initialize_database_skeleton(db)

print('Inserting test data to initialize development environment')
fill_team_about(db)
fill_media_types(db)
fill_categories(db) # added by chris to help test search

create_test_users(db)

fill_digital_media(db)

simulate_test_messages(db)

print('Development database initialization sequence successfully completed.')