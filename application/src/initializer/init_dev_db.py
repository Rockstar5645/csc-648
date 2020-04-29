from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import fill_team_about
from src.initializer.auxiliary_methods import fill_media_types
from src.initializer.auxiliary_methods import fill_digital_media

db = MyDB()

print('Initializing Database skeleton: creating tables')
initialize_database_skeleton(db)

print('Inserting test data to initialize development environment')
fill_team_about(db)
fill_media_types(db)
fill_digital_media(db)

print('Development database initialization sequence successfully completed.')