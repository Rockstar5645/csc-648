1. Start mysql:
	“brew services start mysql”        if on Mac w/ home-brew installed

2. Create new schema in workbench

3. Navigate to test_pkg
	from project directory:
	cd application/father/test_pkg

4. create test db table
	python3 db_create_test_table.py

5. Create 5 test entries
	python3 db_M2_test_fill.py

6. Test
	run the flask app. Click on search, list should populate.