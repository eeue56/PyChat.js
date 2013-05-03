import logging

from pychatjs.server.protocol import create_message, create_disconnect


class Room(object):

    def __init__(self, name=None):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def disconnect(self, user):
        self.remove_user(user)
        self.send_message(create_disconnect(user.id.name))

    @property
    def get_users_connected(self):
        return self.users

    @property
    def user_names(self):
        return [user.id.name for user in self.users]

    @property
    def amount_of_users_connected(self):
        return len(self.users)

    def send_message(self, message):
        for handler in self.users:
            logging.info('Handler: ' + str(handler))
            handler.write_message(message)

    def __str__(self):
        return self.name

    def welcome(self, user):

        self.send_message(create_message('RoomServer', 'Please welcome {name} to the server!\nThere are currently {i} users online -\n {r}\n'.format(name=user.id, 
                          i=self.amount_of_users_connected, 
                          r=' '.join(self.user_names))))
        logging.debug('Welcoming user {user} to {room}'.format(user=user.id.name, room=self.name))

    def __str__(self):
        return 'Name: {name}, users:{users}'.format(name=self.name, users=', '.join(self.users))

    def repr(self):
        return str(self)
