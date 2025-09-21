import sqlite3
from datetime import datetime

class Database():
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        # If table is not created
        table = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='finances';")
        table = table.fetchone()

        if not table:
            self.__create_table()

    def __add_record(self, amount: float, description: str, category: str, date: datetime) -> None:
        self.cursor.execute("INSERT INTO finances(amount, description, category, date) VALUES (?, ?, ?, ?);", (amount, description, category, date))
        self.connection.commit()

    def __delete_record(self, id: int):
        self.cursor.execute("DELETE FROM finances WHERE id=?;", (id,))
        self.connection.commit()

    def __create_table(self) -> None:
        self.cursor.execute("CREATE TABLE finances(id integer primary key, amount real, description varchar(255), category varchar(255), date datetime);")
    def __delete_table(self) -> None:
        self.cursor.execute("DROP TABLE finances;")