from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import fill_team_about
from src.initializer.auxiliary_methods import fill_media_types
from src.initializer.auxiliary_methods import fill_digital_media
from src.initializer.auxil_3 import fill_categories

db = MyDB()

print('Initializing Database skeleton: creating tables')
initialize_database_skeleton(db)

print('Inserting test data to initialize development environment')
fill_team_about(db)
fill_media_types(db)
fill_categories(db) # added by chris to help test search

# create an initial root user, for the digital media entries to reference
print('Creating root user to serve as placeholder owner of digital media entries, and recipient')
db.query("INSERT INTO user (first_name) VALUES (%s)", ('dev_root',))
db.commit()
print('root user created')

# create secondary user to serve as sender of messages
print('Creating secondary user to serve as placeholder owner of digital media entries, and recipient')
db.query("INSERT INTO user (first_name) VALUES (%s)", ('dev_secondary',))
db.commit()
print('secondary user created')

# create an initial default category, for the digital media entries to reference

# commented out by chris, auxil_3.py contains the fill_categories method
'''
print('Creating default category for digital media entries to reference')
db.query("INSERT INTO categories (category) VALUES (%s)", ('art',))
db.commit()
print('default category created')
'''

fill_digital_media(db)

print('Development database initialization sequence successfully completed.')