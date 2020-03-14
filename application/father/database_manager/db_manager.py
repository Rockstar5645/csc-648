from father.database_manager import cnx



class DB:

    def __init__(self):
        self.db_connection = cnx.MyDB()

    def search_like(self, category, term):
        self.db_connection.query("SELECT name, description from digital_media_test WHERE `name` LIKE %s OR `description` LIKE %s", (term, term))
        data = self.db_connection.fetchall()
        self.db_connection.commit()
        return data