import sqlite3

class Conn(object):
    def __init__(self):
        self.connection = sqlite3.connect()

    def insert_new_user(self, username):
        c = self.connection.cursor()
	c.execute("INSERT INTO Users VALUES(?)", (username,))

    def insert_new_message(self, username, room_name, send_time):

	c = self.connnection.cursor()
        if not send_time:
            c.execute("INSERT INTO Messages VALUES(username = ?, room_name = ?)",(username, room_name))
        else:
            c.execute("INSERT INTO Messages VALUES(username = ? room_name = ? send_time = ?)",(username, room_name, send_time))