from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import fill_team_about
from src.initializer.auxiliary_methods import fill_categories

db = MyDB()

initialize_database_skeleton(db)
fill_team_about(db)
fill_categories(db)

# create an initial root user, for the digital media entries to reference
db.query("INSERT INTO user (first_name) VALUES (%s)", ('dev_root',))

add_digital_media_query = ("INSERT INTO digital_media  "
                           "(owner_id, name, description, file_path, thumbnail_path, category, price, approval) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

digital_media_entries = [
    ('1', 'sponge bob 1', 'this is the first test photo', '/M2_test_images/sb1.jpg', '/thumbnails/sb1_t.jpg',
     'image', 99.99, 0),
    ('1', 'sponge bob 2', 'this is the second test photo', '/M2_test_images/sb2.jpg','/thumbnails/sb2_t.jpg' ,\
     'video' , 89.99, 0),
    ('1', 'sponge bob 3', 'this is the third test photo', '/M2_test_images/sb3.jpg','/thumbnails/sb3_t.jpg' ,
     'document' , 79.99, 0),
    ('1', 'sponge bob 4', 'this is the fourth test photo', '/M2_test_images/sb4.jpg','/thumbnails/sb4_t.jpg' ,
     'audio' , 69.99, 0),
    ('1', 'sponge bob 5', 'this is the fifth test photo', '/M2_test_images/sb5.jpg','/thumbnails/sb5_t.jpg' ,
     'image' , 59.99, 0)
]

for digital_media_entry in digital_media_entries:
    db.query(add_digital_media_query, digital_media_entry)
    db.commit()

