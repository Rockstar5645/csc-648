from father.database_manager import cnx

###############################################
#
# NOTE: This file replaces both previous
#
# 1. if the test table exists, it drops the table.
# 2. create a new test table
# 3. fill test table with data
#
##############################################3

db = cnx.MyDB()

# drop existing table
db.query("DROP TABLE IF EXISTS digital_media_test")

# create replacement table
db.query("CREATE TABLE digital_media_test ("
         "media_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "owner_name VARCHAR(50),"
         "name VARCHAR(50),"
         "description VARCHAR(150),"
         "file_path VARCHAR(200),"
         "thumbnail VARCHAR(200),"
         "category VARCHAR(20),"
         "price FLOAT(2),"
         "approval INT,"
         "PRIMARY KEY (media_id))")

# fill db
db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`)"
"VALUES ("
"'username001', 'sponge bob 1', 'this is the first test photo', '/M2_test_images/sb1.jpg', 'image' , 99.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`)"
"VALUES ("
"'username001', 'sponge bob 2', 'this is the second test photo', '/M2_test_images/sb2.jpg', 'video' , 89.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`)"
"VALUES ("
"'username001', 'sponge bob 3', 'this is the third test photo', '/M2_test_images/sb3.jpg', 'document' , 79.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`)"
"VALUES ("
"'username001', 'sponge bob 4', 'this is the fourth test photo', '/M2_test_images/sb4.jpg', 'audio' , 69.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`)"
"VALUES ("
"'username001', 'sponge bob 5', 'this is the fifth test photo', '/M2_test_images/sb5.jpg', 'image' , 59.99, 0"
")")
db.commit()