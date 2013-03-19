import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from random import choice

from server_exceptions import RoomNotFoundException
from room import *

import logging

rooms = [Room('Darkness')]

usernames = ['Shauna', 'Tomuel', 'Darkok']


class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)
    
    def release_name(self):
        usernames.append(self.name)


class ChatConnection(object):
    def __init__(self, username, handler):
        self.id = username
        self._rooms = []
        self.handler = handler
        self.parse_join('join Darkness')
        self.write_message('hello')

    def write_message(self, message):
        logging.debug("Sending message {mes} to {usr}".format(mes=message, usr=self.id))
        self.handler.write_message(message)

    def join_room(self, room_name):        
        logging.debug('Joining room {ro}'.format(ro=room_name))

        for room in rooms:
            if room.name == room_name:
                room.add_user(self)
                self._rooms.append(room)
                return
        raise RoomNotFoundException('No such room as {name}!'.format(name=room_name))

    def _send_to_all_rooms(self, message):
        for room in self._rooms:
            room.send_message(message)

    def parse_nick(self, message):
        logging.info('Parsing nick...')
        previous_name = self.id.name
        self.id.release_name()
        self.id = User(message[message.index('nick') + 4:].strip())
        
        logging.debug('Nick set as {name}'.format(name=self.id))
        self._send_to_all_rooms('User {n} is now known as {nick}\n'.format(n=previous_name, nick=self.id.name))
      
    def parse_join(self, message):
        logging.info('Parsing join...')
        room_name = message[message.index('join') + 4:].strip()

        logging.debug('Room name set as {name}'.format(name=room_name))

        try:
            room = self.join_room(room_name)
            self._rooms.append(room)
            room.welcome(self)
        except RoomNotFoundException:
            logging.debug('Room not found!')
            self.write_message('No such room!\n')

    def close(self):
        self.id.release_name()
        
        for room in self._rooms:
            room.remove_user(self)


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        if len(usernames) > 0:
            id_ = User(choice(usernames))
            usernames.remove(id_.name)
        else:
            id_ = User('Guest {i}'.format(i=len(connections)))

        self.conn = ChatConnection(id_, self)

        logging.info('User with name {name} joined!'.format(name=id_))

        self.write_message('Connected successfully\n')

    def on_message(self, message):
        logging.info('Message {mes} recieved from user {id}'.format(mes=message, 
            id=self.conn.id))

        if message.startswith('\\'):
            if 'nick' in message[:7]:
               self.conn.parse_nick(message)
            elif 'join' in message[:7]:
                self.conn.parse_join(message)
            return 
            
        self.conn._send_to_all_rooms('{id} says: {mes}\n'.format(id=self.conn.id, mes=message))
 
    def on_close(self):
        logging.info('User {id} disconnected!'.format(id=self.conn.id))
        self.conn.close()

        self.write_message('Connection closed')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('wut?')


application = tornado.web.Application([
    (r"/ws", WSHandler),
    (r"/wst", MainHandler),
])

if __name__ == "__main__":
    from time import time
    logging.basicConfig(filename='server.log', level=logging.DEBUG, format="%(asctime)s;  %(levelname)s;  %(message)s")

    logging.info('\n\n\n==========================\nStarted program')
    

    logging.debug('Listening on port 8000...')
    application.listen(8000)
    
    logging.debug('Starting main loop...')
    tornado.ioloop.IOLoop.instance().start()
