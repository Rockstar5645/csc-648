###############################################
#            DIGITAL MEDIA DATA               #
###############################################

digital_media_name = "digital_media_test"

digital_media_column_creator = \
        "media_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT," \
        "owner_id BIGINT UNSIGNED," \
        "name VARCHAR(50), " \
        "description VARCHAR(150)," \
        "file_path VARCHAR(200)," \
        "thumbnail VARCHAR(200)," \
        "category VARCHAR(20)," \
        "price FLOAT(2)," \
        "approval INT," \
        "PRIMARY KEY (media_id)"

digital_media_columns = "`owner_id`, `name`, `description`, `file_path`, `category`, `price`, `approval`"

digital_media_entries = [
    "'1', 'sponge bob 1', 'this is the first test photo', '/M2_test_images/sb1.jpg', 'image' , 99.99, 0",
    "'1', 'sponge bob 2', 'this is the second test photo', '/M2_test_images/sb2.jpg', 'video' , 89.99, 0",
    "'1', 'sponge bob 3', 'this is the third test photo', '/M2_test_images/sb3.jpg', 'document' , 79.99, 0",
    "'1', 'sponge bob 4', 'this is the fourth test photo', '/M2_test_images/sb4.jpg', 'audio' , 69.99, 0",
    "'1', 'sponge bob 5', 'this is the fifth test photo', '/M2_test_images/sb5.jpg', 'image' , 59.99, 0"
]

###############################################
#               CATEGORY DATA                 #
###############################################

categories_name = "categories"

categories_column_creator = \
    "cat_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"\
    "category VARCHAR(50)," \
    "PRIMARY KEY (cat_id)" 

categories_columns = "`category`"

categories_entries = [
    "'all'",
    "'image'",
    "'video'",
    "'audio'",
    "'document'"
]

###############################################
#                 TEAM DATA                   #
###############################################

team_about_name = "team_about"

team_about_column_creator = \
    "team_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT," \
    "name VARCHAR(50)," \
    "link VARCHAR(20)," \
    "position VARCHAR(50)," \
    "image VARCHAR(100)," \
    "description VARCHAR(100)," \
    "facebook VARCHAR(100)," \
    "twitter VARCHAR(100)," \
    "instagram VARCHAR(100)," \
    "linkedin VARCHAR(100)," \
    "PRIMARY KEY (team_id)"

team_about_columns = "`name`, `position`, `link`, `image`, `description`, `facebook`, `twitter`, `instagram`, `linkedin`"

team_about_entries = [
    "'Avery Chen', '/avery', 'Back-end Member', 'static/team_images/avery.jpg', 'Undergraduate student at SFSU', '', '', '', ''",
    "'Akhil Gandu', '/akhil', 'GitHub Master', 'static/team_images/akhil.jpg', 'Graduate Student at SFSU', 'https://www.facebook.com/rockstar290', 'https://twitter.com/Rockstar5645', 'https://www.instagram.com/akhil_gandu/', 'https://www.linkedin.com/in/akhilgandu/'",
    "'Chris Eckhardt', '/chris', 'Back-end lead', 'static/team_images/chris.jpg', 'Undergrad at SFState', '', '', 'https://www.instagram.com/chris_evan_eckhardt/', 'https://www.linkedin.com/in/christopher-eckhardt-04abb1119/'",
    "'Elliot Yardley', '/elliot', 'Front-end lead', 'static/team_images/elliot.jpg', 'Graduate Student, SFSU', '', '', '', ''",
    "'Thomas Yu', '/thomas', 'Front End Member', 'static/team_images/Thomas.jpg', 'Undergraduate Student, SFSU', '', '', '', ''",
    "'Bakulia Kurmant', '/bakulia', 'Team Lead', 'static/team_images/bakulia.jpg', 'In my spare time I like going outdoors, techno music, reading, traveling', '', '', 'https://www.instagram.com/bakuliak/?hl=en', 'https://www.linkedin.com/in/bakulia-kurmant/'"
]