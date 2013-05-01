#!/usr/bin/env python

import MySQLdb

class MessageInterface(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="slmentor", passwd="slmentor77", db="mentor")

    def insert_message(self, message, user_ID, event_ID, message_ID):
        cur = self.db.cursor()
        cur.execute("INSERT INTO messages(Message_id, Message) VALUES(%s, %s)",(message_ID, message))
        cur.execute("INSERT INTO message_by(User_id, Event_id, Message_id) VALUES(%s,%s,%s)", (user_ID, event_ID, message_ID))

    def get_message(self, message_ID):
        cur = self.db.cursor()
        cur.execute("SELECT Message FROM messages WHERE messages.Message_id=?",(message_ID))
        return cur.fetchall()

    def get_events(self, event_ID):
        cur = self.db.cursor()
        cur.execute("""SELECT message_by.User_id, messages.Message, messages.Time 
                        FROM message_by 
                        LEFT JOIN messages ON message_by.Message_id 
                        WHERE message_by.Event_id=?
                        ORDER BY messages.Time""", (event_ID,))
        return cur.fetchall()

    def get_all_user_messages(self, user_ID):
        cur = self.db.cursor()
        cur.execute

    def get_message_time(self,table):
        print "help"

if __name__ == "__main__":
    connection = MessageInterface()
    connection.insert_message("hello world!", 1, 1, 1)
