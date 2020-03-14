from father.database_manager import cnx

db = cnx.MyDB()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`)"
"VALUES ("
"'username001', 'sponge bob 1', 'this is the first test photo', '/father/test/M2_test_images/sb1.jpg', 'picture' , 99.99"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`)"
"VALUES ("
"'username001', 'sponge bob 2', 'this is the second test photo', '/father/test/M2_test_images/sb2.jpg', 'picture' , 89.99"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`)"
"VALUES ("
"'username001', 'sponge bob 3', 'this is the third test photo', '/father/test/M2_test_images/sb3.jpg', 'picture' , 79.99"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`)"
"VALUES ("
"'username001', 'sponge bob 4', 'this is the fourth test photo', '/father/test/M2_test_images/sb4.jpg', 'picture' , 69.99"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`)"
"VALUES ("
"'username001', 'sponge bob 5', 'this is the fifth test photo', '/father/test/M2_test_images/sb5.jpg', 'picture' , 59.99"
")")
db.commit()
