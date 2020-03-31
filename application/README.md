# Application Folder

1) package setup
    1.a) navigate to application folder
    1.b) run command 'pip install -e' in terminal
    1.c) delete 'father_egg' directory that is created

2) setup test
    2.a) install and run mysql
    2.b) open workbench and create schema called 'snapster'
    2.c) create a file called 'config.py' inside of 'father' directory
    2.d) copy and paste the following inside of 'config.py':
    db_conn = {
        'user': 'root',
        'password' : '[YOUR PASSWORD HERE]',
        'host' : '127.0.0.1',
        'port' : '3306',
        'database' : 'snapster'
    }
    2.e) replace [YOUR PASSWORD HERE] with your password.

3) run program
    3.a) from inside application, run the command 'python3 run.py'
