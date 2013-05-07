
class UsernameInUseException(Exception):
    pass


class User(object):
    def __init__(self, server, name=None):
        if name is None:
            name = server.temp_name
        self.name = name
        self.server = server

    def __str__(self):
        return str(self.name)

    def _to_json(self):
        return self.__dict__
    
    def release_name(self):
        self.server.release_name(self.name)
        
    def change_name(self, username):
        self.release_name()

        try:
            self.server.register_name(username)
        except UsernameInUseException:
            logging.log(', '.join(self.server.registered_names))
            self.server.register_name(self.name)
            raise
            
        self.name = username


class UserServer(object):

    def __init__(self, names=None):
        if names is None:
            names = ['a', 'b', 'c', 'd', 'e']
        self.temp_names = names
        self.registered_names = []

    @property
    def temp_name(self):
        return self.temp_names.pop(0)

    def is_username_used(self, username):
        return username in self.registered_names

    def register_name(self, username):
        if self.is_username_used(username):
            raise UsernameInUseException('Username {username} already in use!'.format(username=username))
        self.registered_names.append(username)


    def release_name(self, username):
        self.temp_names.append(username)
        if self.is_username_used(username):
            self.registered_names.remove(username)