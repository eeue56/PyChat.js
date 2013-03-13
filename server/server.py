import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from random import choice


connections = []

usernames = ['Shauna', 'Tomuel', 'Darkok']

class User(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
    	if len(usernames) > 0:
    		self.id = User(choice(usernames))
    		usernames.remove(self.id.name)
    	else:
    		self.id = User('Guest {i}'.format(i=len(connections)))

    	connections.append(self)

        print 'new connection'

        self.write_message("There are currently {con} connections\n\n".format(con=len(connections)))
        
      
    def on_message(self, message):
    	print message
        for con in connections:
        	con.write_message('{id} says: {mes}\n'.format(id=self.id.name, mes=message))
 
    def on_close(self):
    	usernames.append(self.id.name)
    	connections.remove(self)
        print 'connection closed'




application = tornado.web.Application([
    (r"/ws", WSHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
