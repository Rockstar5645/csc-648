from src.database_manager.database_connection import MyDB
from src.initializer.initialize_database_skeleton import initialize_database_skeleton
from src.initializer.auxiliary_methods import fill_team_about
from src.initializer.auxiliary_methods import fill_categories

db = MyDB()

initialize_database_skeleton(db)
fill_team_about(db)
fill_categories(db)