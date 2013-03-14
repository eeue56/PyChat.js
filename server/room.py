class Room(object):

    def __init__(self, name=None):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    @property
    def get_users_connected(self):
        return self.users

    @property
    def user_names(self):
        return [user.id for user in self.users]

    @property
    def amount_of_users_connected(self):
        return len(self.users)

    def send_message(self, message):
        for handler in self.users:
            handler.write_message(message)

    def welcome(self, user):
        self.send_message('Please welcome {name} to the server!'.format(name=user.id))