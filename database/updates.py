import sqlite3

class Conn(object):
    def __init__(self):
        self.connection = sqlite3.connect()

    def insert_new_user(self, username):
        c = self.connection.cursor()
        c.execute("INSERT INTO Users VALUES(?)", (username,))
        connection.commit()

    def insert_new_message(self, username, room_name):
       c = self.connnection.cursor()
       c.execute("INSERT INTO Messages VALUES(username = ?, room_name = ?)",(username, room_name))
       connection.commit()

    def insert_new_room(self, room_name):
        c = self.connection.cursor()
        c.execute("INSERT INTO Rooms VALUES(room_name = ?)", (room_name,))
        connection.commit()