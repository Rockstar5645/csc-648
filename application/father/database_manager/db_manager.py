from father.database_manager import cnx



class DB:


    def __init__(self):
        db_connection = cnx.MyDB()

    def search_like(self, category, term):
        # this is just a test, it will return the values sent from the form
        return([category, term])

