from src.database_manager import cnx
from src.database_manager.objects.table import DBTable
from src.test_pkg.table_data import *

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
###############################################

db = cnx.MyDB()

###############################################
#            CREATE TABLE OBJECTS             #
###############################################

dm_table = DBTable(digital_media_name, digital_media_column_creator, digital_media_columns, digital_media_entries)
cat_table = DBTable(categories_name, categories_column_creator, categories_columns, categories_entries)
team_table = DBTable(team_about_name, team_about_column_creator, team_about_columns, team_about_entries)

tables = [dm_table, cat_table, team_table]

###############################################
#             DROP TABLES FROM DB             #
###############################################
for table in tables:
    db.query(table.drop_table_string())

###############################################
#           CREATE TABLES IN DB               #
###############################################
for table in tables:
    db.query(table.create_table_string())

###############################################
#            FILL TABLES IN DB                #
###############################################
for table in tables:
    for entry in table.get_entries():
        db.query(table.insert_row(entry))
        db.commit()

############################
#         USER TABLE       #
############################

db.query("DROP TABLE IF EXISTS user")

db.query("CREATE TABLE IF NOT EXISTS user ("
         "user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
         "first_name VARCHAR(30),"
         "last_name VARCHAR(30),"
         "email VARCHAR(20),"
         "phone_number VARCHAR(10),"
         "username VARCHAR(20) UNIQUE,"
         "password BINARY(60),"
         "PRIMARY KEY (user_id))")
