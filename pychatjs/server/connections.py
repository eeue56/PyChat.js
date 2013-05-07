import logging
from pychatjs.server.room import Room


class ChatConnection(object):
    """
        Chat connection object used to store -
            User id
            The handler
            Rooms connected
            The possible rooms, which should be a shared list

            TODO: Move rooms to room server
    """
    def __init__(self, username, handler, rooms):
        self.id = username
        self._rooms = {}
        self.handler = handler
        self.rooms = rooms

    def write_message(self, message):
        """ Writes a message to this chat connection's handler """
        logging.debug("Sending message {mes} to {usr}".format(mes=message, usr=self.id))
        self.handler.write_message(message)

    def join_room(self, room_name):   
        """ Connects to a given room 
                If it does not exist it is created"""     
        logging.debug('Joining room {ro}'.format(ro=room_name))

        for room in self.rooms:
            if room.name == room_name:
                room.add_user(self)
                self._rooms[room_name] = room
                room.welcome(self)
                break
        else:
            room = Room(room_name)
            self.rooms.append(room)
            self._rooms[room_name] = room
            room.add_user(self)

    def send_to_room(self, message, room_name):
        """ Sends a given message to a given room """
        room = self.get_room(room_name)

        if room is not None:
            room.send_message(message)

    def _send_to_all_rooms(self, message):
        """ Send a message to all connected rooms """
        for room in self._rooms.values():
            room.send_message(message)

    def close(self):
        """ Closes the connection by removing the user from all rooms """
        logging.debug('Closing for user {user}'.format(user=self.id.name))
        self.id.release_name()
        for room in self._rooms.values():
            room.disconnect(self)

    @property
    def possible_rooms(self):
        """ Returns possible rooms for this connection """
        return self.rooms

    def get_room(self, room_name):
        """ Gets the room with the given name if connected """
        try:
            return self._rooms[room_name]
        except KeyError:
            return None
