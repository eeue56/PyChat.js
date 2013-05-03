import logging
from pychatjs.server.room import Room

rooms = [Room('Darkness')]


class ChatConnection(object):
    def __init__(self, username, handler):
        self.id = username
        self._rooms = {}
        self.handler = handler

    def write_message(self, message):
        logging.debug("Sending message {mes} to {usr}".format(mes=message, usr=self.id))
        self.handler.write_message(message)

    def join_room(self, room_name):        
        logging.debug('Joining room {ro}'.format(ro=room_name))

        for room in rooms:
            if room.name == room_name:
                room.add_user(self)
                self._rooms[room_name] = room
                room.welcome(self)
                break
        else:
            room = Room(room_name)
            rooms.append(Room(room_name))
            self._rooms[room_name] = room
            room.add_user(self)

    def send_to_room(self, message, room_name):
        room = get_room(room_name)

        if room is not None:
            room.send_message(message)

    def _send_to_all_rooms(self, message):
        for room in self._rooms:
            room.send_message(message)

    def close(self):
        logging.debug('Closing for user {user}'.format(user=self.id.name))
        self.id.release_name()
        for room in self._rooms.values():
            room.remove_user(self)

    @property
    def possible_rooms(self):
        return rooms

    def get_room(self, room_name):
        try:
            return self._rooms[room_name]
        except KeyError:
            return None
