import logging

from pychatjs.server.protocol import *
from pychatjs.server.user_server import UsernameInUseException


class Parser(object):
    """ Parser to be used and extended to handle more things 

        TODO: Change to use dict to allow easy extension"""
    def __init__(self, connection):
        self.connection = connection
        self.functions = {'ping' : self.ping, 
            'roomlist' : self.roomlist, 
            'join' : self.join,
            'userlist' : self.userlist,
            'send' : self.send,
            'get_user_dump' : self.get_user_dump,
            'get_users_dump' : self.get_users_dump,
            'send_dump' : self.send_dump,
            'next_slide' : self.next_slide,
            'previous_slide' : self.previous_slide,
            'request_name' : self.request_name}


    def parse_message(self, message):  
        """ Parse a given message and run the command using the 
            connection and the json protocals """      

        service = None

        try:
            service = get_service(message)
        except ValueError:
            pass

        conn = self.connection

        # check if valid request
        if service is None or service not in requests.keys():
            logging.info('No such request!')
            conn.write_message(create_error('1', 'no such request'))
            return

        request_name = requests[service]
        data = get_data(message)

        logging.debug(data)

        self.functions[request_name](data)

    def ping(self, data):
        conn.write_message(create_pong())

    def roomlist(self, data):
        conn.write_message(create_roomlist(conn.possible_rooms))
        
    def join(self, data):
        logging.debug("Name is " + conn.id.name)
        logging.debug("Name should be " + data['username'])
        if conn.id.name != data['username']:   
            try:             
                conn.id.change_name(data['username'])
            except UsernameInUseException:
                conn.write_message(create_error(2, 'Username was already in use!'))
        conn.join_room(data['room'])
        conn._send_to_all_rooms(create_connect(conn.id.name))
    
    def userlist(self, data):
        room = conn.get_room(data['room'])
        if room is None:
            conn.write_message('No such room as {room}'.format(room=data['room']))
        else:
            conn.write_message(create_userlist(room.user_names))
    
    def send(self, data):
        room = conn.get_room(data['room'])
        if room is not None:
            room.send_message(create_message(data['username'], data['message']))
    
    def get_user_dump(self, data):
        username = data['username']
        for room in conn.possible_rooms:
            if room.get_user(username) is not None:
                conn.write_message(create_user_dump(room.get_user(username)))
                break
        else:
            conn.write_message(create_error(3, 'User not found in any active rooms'))
    
    def get_users_dump(self, data):
        room = conn.get_room(data['room'])
        if room is not None: 
            conn.write_message(create_users_dump(room.get_users_connected))
    
    def send_dump(self, data):
        for prop, value in data.iteritems():
            setattr(conn.id, prop, value)
    
    def next_slide(self, data):
        room = conn.get_room(data['room'])
        room.send_message(create_next_slide())
    
    def previous_slide(self, data):
        room = conn.get_room(data['room'])
        room.send_message(create_previous_slide())
    
    def request_name(self, data):
        room = conn.get_room(data['room'])
        room.send_message(create_jump_to(data['slideNumber']))
    