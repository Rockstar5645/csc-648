from father.database_manager import cnx

db = cnx.MyDB()

############################
#         USER TABLE       #
############################

db.query("CREATE TABLE IF NOT EXISTS user ("
         "user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "first_name VARCHAR(30),"
         "last_name VARCHAR(30),"
         "email VARCHAR(20),"
         "phone_number VARCHAR(10),"
         "username VARCHAR(20),"
         "password BINARY(60),"
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

###############################
#      TEAM ABOUT TABLE       #
###############################

db.query("CREATE TABLE IF NOT EXISTS team_about ("
        "team_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
        "name VARCHAR(50),"
        "link VARCHAR(20),"
        "position VARCHAR(50),"
        "image VARCHAR(100),"
        "description VARCHAR(100),"
        "facebook VARCHAR(100),"
        "twitter VARCHAR(100),"
        "instagram VARCHAR(100),"
        "linkedin VARCHAR(100),"
        "PRIMARY KEY (team_id))")

###############################
#     FILL TEAM ABOUT TABLE   #
###############################

# Avery
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Avery Chen', '/avery', 'Back-end Member', 'static/team_images/avery.jpg', 'Undergraduate student at SFSU', '', '', '', ''"
        ")")
db.commit()

# Akhil
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Akhil Gandu', '/akhil', 'GitHub Master', 'static/team_images/akhil.jpg', 'Graduate Student at SFSU', 'https://www.facebook.com/rockstar290', 'https://twitter.com/Rockstar5645', 'https://www.instagram.com/akhil_gandu/', 'https://www.linkedin.com/in/akhilgandu/'"
        ")")
db.commit()

# Chris
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Chris Eckhardt', '/chris', 'Back-end lead', 'static/team_images/chris.jpg', 'Undergrad @ SFState', '', '', 'https://www.instagram.com/chris_evan_eckhardt/', 'https://www.linkedin.com/in/christopher-eckhardt-04abb1119/'"
        ")")
db.commit()

# Elliot
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Elliot Yardley', '/elliot', 'Front-end lead', 'static/team_images/elliot.jpg', 'Graduate Student, SFSU'', '', '', '', ''"
        ")")
db.commit()

# Thomas
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Thomas Yu', '/thomas', 'Front End Member', 'static/team_images/Thomas.jpg', 'Undergraduate Student, SFSU', '', '', '', ''"
        ")")
db.commit()

#Bakulia
db.query("INSERT INTO team_about ("
        "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`),"
        "VALUES ("
        "'Bakulia Kurmant', '/bakulia', 'Team Lead', 'static/team_images/bakulia.jpg', 'In my spare time I like going outdoors, techno music, reading, traveling', '', '', 'https://www.instagram.com/bakuliak/?hl=en', 'https://www.linkedin.com/in/bakulia-kurmant/'"
        ")")
db.commit()

