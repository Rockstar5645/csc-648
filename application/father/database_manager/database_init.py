from father.database_manager import cnx

db = cnx.MyDB()

# if a table already exits in your database just comment it out!!!

############################
#         USER TABLE       #
############################

db.query("CREATE TABLE IF NOT EXISTS user ("
         "user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "first_name VARCHAR(30),"
         "last_name VARCHAR(30),"
         "email VARCHAR(20),"
         "phone_number VARCHAR(10),"
         "PRIMARY KEY (user_id))")

###############################
#      DIGITAL MEDIA TABLE    #
###############################

db.query("CREATE TABLE IF NOT EXISTS digital_media ("
         "media_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "owner_id BIGINT UNSIGNED NOT NULL,"
         "name VARCHAR(50),"
         "description VARCHAR(150),"
         "file_path VARCHAR(200),"
         "thumbnail VARCHAR(200),"
        "time_stamp DATE,"
        "category VARCHAR(20),"
        "price FLOAT(2),"
        "PRIMARY KEY (media_id),"
        "FOREIGN KEY (owner_id) REFERENCES user (user_id))")

###############################
#      CATEGORIES TABLE       #
###############################

db.query("CREATE TABLE IF NOT EXISTS categories ("
         "cat_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "category VARCHAR(50),"
         "PRIMARY KEY (cat_id))")

############################
#      FILL CATEGORIES     #
############################

db.query("INSERT INTO categories ("
"`category`)"
"VALUES ("
"'all'"
")")
db.commit()

db.query("INSERT INTO categories ("
"`category`)"
"VALUES ("
"'image'"
")")
db.commit()

db.query("INSERT INTO categories ("
"`category`)"
"VALUES ("
"'video'"
")")
db.commit()

db.query("INSERT INTO categories ("
"`category`)"
"VALUES ("
"'audio'"
")")
db.commit()

db.query("INSERT INTO categories ("
"`category`)"
"VALUES ("
"'document'"
")")
db.commit()