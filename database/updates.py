import sqlite3

class database_connection:
    __init__(self):
        self.connection = sqlite3.connect()

    def insert_new_user(self, username):
        self.connection.execute("INSERT INTO Users VALUES(?)", (username))

    def insert_new_message(self, username, roomName, sendTime):
        if not sendTime:
            self.connection.execute("INSERT INTO Messages VALUES(username = ?, roomName = ?)",(username, roomName))
        else:
            self.connection.execute("INSERT INTO Messages VALUES(username = ? roomName = ? sendTime = ?)",(username, roomName, sendTime))
