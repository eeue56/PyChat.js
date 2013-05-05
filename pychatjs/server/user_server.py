
class UsernameInUseException(Exception):
	pass

class User(object):
    def __init__(self, name, server):
        self.name = name
        self.server = server

    def __str__(self):
        return str(self.name)
    
    def release_name(self):
    	self.server.release_name(self.name)
        
    def change_name(self, username):
    	self.release_name()

    	try:
    		self.server.register_name(username)
    	except UsernameInUseException:
    		self.server.register_name(name)
    		raise
    		
    	self.name = username



class UserServer(object):

	def __init__(self):
		self.registered_names = []

	def is_username_used(self, username):
		return username in self.registered_names

	def register_name(self, username):
		if self.is_username_used(username):
			raise UsernameInUseException('Username {username} already in use!'.format(username=username))
		self.registered_names.append(username)

	def release_name(self, username):
		self.registered_names.remove(username)
