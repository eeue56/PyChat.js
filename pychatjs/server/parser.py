import logging

from pychatjs.server.protocol import *
from pychatjs.server.user_server import UsernameInUseException


class Parser(object):
    """ Parser to be used and extended to handle more things 

        TODO: Change to use dict to allow easy extension"""
    def __init__(self, connection):
        self.connection = connection


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

        # process requests without data
        if request_name == 'ping':
            conn.write_message(create_pong())
            return
        elif request_name == 'roomlist':
            conn.write_message(create_roomlist(conn.possible_rooms))
            return


        data = get_data(message)

        logging.debug(data)

        # process requests with data
        
        if request_name == 'join':
            logging.debug("Name is " + conn.id.name)
            logging.debug("Name should be " + data['username'])
            if conn.id.name != data['username']:   
                try:             
                    conn.id.change_name(data['username'])
                except UsernameInUseException:
                    conn.write_message(create_error(2, 'Username was already in use!'))
            conn.join_room(data['room'])
            conn._send_to_all_rooms(create_connect(conn.id.name))

        elif request_name == 'userlist':
            room = conn.get_room(data['room'])

            if room is None:
                conn.write_message('No such room as {room}'.format(room=data['room']))
            else:
                conn.write_message(create_userlist(room.user_names))

        elif request_name == 'send':
            room = conn.get_room(data['room'])

            if room is not None:
                room.send_message(create_message(data['username'], data['message']))

        elif request_name == 'get_user_dump':
            username = data['username']
            for room in conn.possible_rooms:
                if room.get_user(username) is not None:
                    conn.write_message(create_user_dump(room.get_user(username)))
                    break
            else:
                conn.write_message(create_error(3, 'User not found in any active rooms'))

        elif request_name == 'get_users_dump':
            room = conn.get_room(data['room'])

            if room is not None: 
                conn.write_message(create_users_dump(room.get_users_connected))

        elif request_name == 'send_dump':
            for prop, value in data.iteritems():
                setattr(conn.id, prop, value)

        elif request_name == 'next_slide':
            room = conn.get_room(data['room'])
            room.send_message(create_next_slide())
       
        elif request_name == 'previous_slide':
            room = conn.get_room(data['room'])
            room.send_message(create_previous_slide())
       
        elif request_name == 'jump_to_slide':
            room = conn.get_room(data['room'])
            room.send_message(create_jump_to(data['slideNumber']))