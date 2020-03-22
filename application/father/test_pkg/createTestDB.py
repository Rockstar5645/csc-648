from father.database_manager import cnx

###############################################
#
# NOTE: This file replaces both previous
#
# 1. if the test table exists, it drops the table.
# 2. create a new test tables
# 3. fills test tables with data
#
# test tables:
# test db table,
# team about table (will carry over)
#
##############################################3

db = cnx.MyDB()

###############################
#       DROP ALL TABLES       #
###############################
db.query("DROP TABLE IF EXISTS digital_media_test")
db.query("DROP TABLE IF EXISTS team_about")
db.query("DROP TABLE IF EXISTS categories")
# db.query("DROP TABLE IF EXISTS team_about")


#######################################
#      DIGITAL MEDIA TEST TABLE       #
#######################################
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


#######################################
#       FILL DIGITAL MEDIA TEST       #
#######################################
db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`"
") VALUES ("
"'username001', 'sponge bob 1', 'this is the first test photo', '/M2_test_images/sb1.jpg', 'image' , 99.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`"
") VALUES ("
"'username001', 'sponge bob 2', 'this is the second test photo', '/M2_test_images/sb2.jpg', 'video' , 89.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`"
") VALUES ("
"'username001', 'sponge bob 3', 'this is the third test photo', '/M2_test_images/sb3.jpg', 'document' , 79.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`"
") VALUES ("
"'username001', 'sponge bob 4', 'this is the fourth test photo', '/M2_test_images/sb4.jpg', 'audio' , 69.99, 0"
")")
db.commit()

db.query("INSERT INTO digital_media_test ("
"`owner_name`, `name`, `description`, `file_path`, `category`, `price`, `approval`"
") VALUES ("
"'username001', 'sponge bob 5', 'this is the fifth test photo', '/M2_test_images/sb5.jpg', 'image' , 59.99, 0"
")")
db.commit()

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

'''
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
'''