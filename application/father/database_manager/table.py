


class DBTable(object):

    def __init__(self, name, column_creator, columns, entries):
        self._name = name
        self._column_creator = column_creator
        self._columns = columns
        self._entries = entries

    def get_entries(self):
        return self._entries

    def drop_table_string(self):
        return "DROP TABLE IF EXISTS " + self._name

    def create_table_string(self):
        return "CREATE TABLE IF NOT EXISTS " + self._name + "(" + self._column_creator + ")"

    def insert_row(self, row):
        return "INSERT INTO " + self._name + " (" + self._columns + ") VALUES (" + row + ")"