import logging
from pychatjs.server.room import Room


class ChatConnection(object):
    """
        Chat connection object used to store -
            User id
            The handler
            Rooms connected
    """

    def __init__(self, username, handler, rooms):
        self.id = username
        self._rooms = {}
        self.rooms = rooms
        self.handler = handler

    def write_message(self, message):
        """ Writes a message to this chat connection's handler"""
        logging.debug("Sending message {mes} to {usr}".format(
            mes=message, 
            usr=self.id))
        self.handler.write_message(message)

    def join_room(self, room_name):
        """ Connects to a given room 
            If it does not exist it is created"""      
        logging.debug('Joining room {ro}'.format(ro=room_name))

        for room in ROOMS:
            if room.name == room_name:
                room.add_user(self)
                self._rooms[room_name] = room
                room.welcome(self)
                break
        else:
            room = Room(room_name)
            ROOMS.append(Room(room_name))
            self._rooms[room_name] = room
            room.add_user(self)

    def send_to_room(self, message, room_name):
        """ Send a message to the room """
        room = self.get_room(room_name)

        if room is not None:
            room.send_message(message)

    def _send_to_all_rooms(self, message):
        """ Send a message to all connected rooms"""
        for room in self._rooms:
            room.send_message(message)

    def close(self):
        """ Closes the connection by removing the user from all rooms """
        self.id.release_name()
        for room in self._rooms.values():
            room.remove_user(self)

    @property
    def possible_rooms(self):
        """ Returns all possible rooms"""
        return ROOMS

    def get_room(self, room_name):
        """ Get a given room or None """
        try:
            return self._rooms[room_name]
        except KeyError:
            return None
