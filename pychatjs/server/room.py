import logging

from pychatjs.server.protocol import create_message, create_disconnect


class Room(object):
    """ Room class for holding chat connections and room name
        Acts as room server for now """
    def __init__(self, name=None):
        self.name = name
        self.users = []

    def add_user(self, user):
        """ add a user to users """
        self.users.append(user)

    def remove_user(self, user):
        """ removes a user """
        self.users.remove(user)

    def disconnect(self, user):
        """ Disconnect a user and send a message to the 
            connected clients """
        self.remove_user(user)
        self.send_message(create_message('RoomServer', 'Please all say goodbye to {name}!'.format(name=user.id.name)))
        self.send_message(create_disconnect(user.id.name))

    def get_user(self, username):
        """ gets a user with given username if connected """
        for user in self.users:
            if user.name == username:
                return user
        return None

    @property
    def get_users_connected(self):
        """ get the users connected """
        return self.users

    @property
    def user_names(self):
        """ get the usernames of the users connected """
        return [user.id.name for user in self.users]

    @property
    def amount_of_users_connected(self):
        """ get the amount of users connected """
        return len(self.users)

    def send_message(self, message):
        """ send a message to each of the users """
        for handler in self.users:
            logging.info('Handler: ' + str(handler))
            handler.write_message(message)

    def welcome(self, user):
        """ welcomes a user to the roomserver """
        self.send_message(create_message('RoomServer', 'Please welcome {name} to the server!\nThere are currently {i} users online -\n {r}\n'.format(name=user.id, 
                          i=self.amount_of_users_connected, 
                          r=' '.join(self.user_names))))
        logging.debug('Welcoming user {user} to {room}'.format(user=user.id.name, room=self.name))

    def __str__(self):
        return 'Name: {name}, users:{users}'.format(name=self.name, users=', '.join(self.users))

    def repr(self):
        return str(self)
