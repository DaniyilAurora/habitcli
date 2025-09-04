import sqlite3
import datetime

class Database():
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

        #self.cursor.execute("CREATE TABLE habits(id integer primary key, habit varchar(255), time integer, regularity varchar(255))")
        #self.cursor.execute("DROP TABLE habits")
        #self.cursor.execute("INSERT INTO habits VALUES (1, 'Run', 1, '1d')")
        #self.connection.commit()

    def add_habit(self, habit: str, time: int, regularity: str):
        if time > 23 or time < 0:
            raise Exception("Time cannot be less than 0 and more than 23. (0-23)")
        elif regularity[len(regularity)-1] != "d":
            raise Exception("Regularity should be in format {days}d, eg. 2d")
        
        self.cursor.execute("INSERT INTO habits (habit, time, regularity) VALUES (?, ?, ?)", (habit, time, regularity))
        self.connection.commit()