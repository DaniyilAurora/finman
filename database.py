import sqlite3

class Database():
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        # If table is not created
        table = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='finances';")
        table = table.fetchone()

        if not table:
            self.__create_table()

    def __create_table(self) -> None:
        self.cursor.execute("CREATE TABLE finances(amount real, description varchar(255), category varchar(255), date datetime)")
    def __delete_table(self) -> None:
        self.cursor.execute("DROP TABLE finances")