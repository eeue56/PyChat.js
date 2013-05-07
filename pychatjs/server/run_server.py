import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from random import choice

from pychatjs.server.server_exceptions import RoomNotFoundException
from pychatjs.server.room import *
from pychatjs.server.connections import ChatConnection
from pychatjs.server.parser import Parser
from pychatjs.server.user_server import User, UserServer 

import logging


# default room list - change to add more rooms by default
rooms = [Room('Darkness'), Room('Lightness'), Room('Official')]

# default name list - used to handle multiple connections at once. 
# the number of *new* connections that can be handled at one time is equal to the
# number of names in the list
# anything can be used, however this format allows for easy debugging. 
usernames = ['Shauna', 'Tomuel', 'Darkok', 'Endl', 'Frumo']

user_server = UserServer(names=usernames[:])


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'

        self.write_message('Connected successfully\n')

        # set a temp name
        id_ = User(user_server)

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
