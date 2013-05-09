class UsernameInUseException(Exception):
    pass


class User(object):
    """ Class used to hold a user and the user server """
    def __init__(self, server, name=None):
        if name is None:
            name = server.temp_name
        self.name = name
        self.server = server

    def __str__(self):
        return str(self.name)

    def _to_json(self):
        """ Gets a dict of this object's properties so that it can be used to send a dump to the client """
        return self.__dict__
    
    def release_name(self):
        """ release the username from the user server """
        self.server.release_name(self.name)
        
    def change_name(self, username):
        """ changes the username to given username, throws exception if username used """
        self.release_name()

        try:
            self.server.register_name(username)
        except UsernameInUseException:
            logging.log(', '.join(self.server.registered_names))
            self.server.register_name(self.name)
            raise
            
        self.name = username


class UserServer(object):
    """ User server used to manage names """
    def __init__(self, names=None):
        if names is None:
            names = ['a', 'b', 'c', 'd', 'e']
        self.temp_names = names
        self.registered_names = []

    @property
    def temp_name(self):
        """ gets the top temp name """
        return self.temp_names.pop(0)

    def is_username_used(self, username):
        """ checks if username is used """
        return username in self.registered_names

    def register_name(self, username):
        """ register a name """
        if self.is_username_used(username):
            raise UsernameInUseException('Username {username} already in use!'.format(username=username))
        self.registered_names.append(username)


    def release_name(self, username):
        """ release a name and add it to the temp list """
        self.temp_names.append(username)
        if self.is_username_used(username):
            self.registered_names.remove(username)
