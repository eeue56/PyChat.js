import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from random import choice

from pychatjs.server.server_exceptions import RoomNotFoundException
from pychatjs.server.room import *

import logging

from pychatjs.server.connections import ChatConnection
from pychatjs.server.parser import Parser

rooms = [Room('Darkness')]

usernames = ['Shauna', 'Tomuel', 'Darkok']


class User(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)
    
    def release_name(self):
        usernames.append(self.name)


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'

        self.write_message('Connected successfully\n')

        # set a temp name
        if len(usernames) > 0:
            id_ = User(choice(usernames))
            usernames.remove(id_.name)
        else:
            id_ = User('Guest {i}'.format(choice('abcdefgjklmnopqrsty')))

        self.connection = ChatConnection(id_, self, rooms)
        self.parser = Parser(self.connection)

        logging.info('User with name {name} joined!'.format(name=id_))

    def on_message(self, message):
        logging.info('Message {mes} recieved from user {id}'.format(mes=message, 
            id=self.parser.connection.id))

        self.parser.parse_message(message)
    
    def on_close(self):
        logging.info('User {id} disconnected!'.format(id=self.parser.connection.id))
        self.connection.close()


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
