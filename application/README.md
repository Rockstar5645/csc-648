# Application Folder

1) Package Setup

    1.a) navigate to application folder
    1.b) run command 'pip install -e .' in terminal
    1.c) delete 'src_egg' directory that is created

2) Configuring our Environment

    2.a) install and run mysql (Mac: brew services start mysql)
    2.b) open workbench and create schema called 'snapster'
    2.c) create a file called 'config.py' inside of 'src' directory
    2.d) copy and paste the following inside of 'config.py':
    2.e) replace [YOUR PASSWORD HERE] with your password.
    2.f) update the STATIC_PATH [PATH TO] with your absolute path.
    
    db_conn = {
        'user': 'root',
        'password' : '[YOUR PASSWORD HERE]',
        'host' : '127.0.0.1',
        'port' : '3306',
        'database' : 'snapster'
    }

    redis_conn = {
        'host': 'redis.snapsster.com',
        'password': 'vJB2KVAZs6+2x4i9eVBHp0PZeX1TjX/qPhdgomjNvczK0q0DCtfg5dHxKveLdNmFFZU1yw7z/E/ZcdmI',
        'port': '6379',
        'socket_timeout': 3
    }

    session_duration = 3600


    STATIC_PATH = '[PATH TO] csc648-fa20-team06/application/src/app_pkg/static/'
   


3) Fill database with test data

    - Within the test_pkg, run the fill_db script to initialize the database with sample test data

4) run program

    4.a) from inside application, run the command 'python3 run.py'


Application

    This is where all of our project source code resides.

SRC :
    Contains the major components of our application

    - App_pkg
    - Database_manager
    - Test_pkg
    - Run.py (application launcher)

App_pkg :

	This contains all code related to the flask server and flask application. Routing, forms, static file structure, front-end components, and the flask application itself.

    - Routing : this handles all requests from the client. directing, redirecting, handling forms data, and making requests to the database
    - Templates : this contains all html, css and other front end related files
    - Static : this is going to contain all of our static content. User media, media thumbnails, etc.
    - Forms.py : defines all forms used for user input, these forms can be directly inserted into html files
    - __init__.py is where our flask application is created and lives. Routes are served from this file’s location in VAS

Database_manager :

	All requests for database and redis queries have to go through the database API defined here. There should be no direct connection between the flask application and the database.

    - cnx is the module that defines the class used to manage the connection to the mysql server
    - redis_cnx is the module that defines the class used to manage the connection to the redis server
    - Database_init is the initialization script for the database, which will populate and configure the database with its initial state when deployed in production
    - Db_manager is the module that defines the class which defines the API for interacting with the database
    - Register_login is the module that defines the registration and login api
    - Table_data is the utility script to the database initialization script which contains the initial data to insert into our tables

Test_pkg :

	This contains testing scripts and files to define tables for testing

    - Fill_db: this creates the table objects, drops tables, create tables, and fills tables for digital_media, categories, and team data
    - test_pkg/Table_data:  is the utility script to the database initialization script which contains the initial data to insert into our tables for testing
    - Authentication_test is the script used to test our registration and login functionality