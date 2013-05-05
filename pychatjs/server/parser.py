import logging

from pychatjs.server.protocol import *


class Parser(object):

    def __init__(self, connection):
        self.connection = connection

    def parse_message(self, message):        
        service = None

        try:
            service = get_service(message)
        except ValueError:
            pass

        conn = self.connection

        if service is None or service not in requests.keys():
            logging.info('No such request!')
            conn.write_message(create_error('1', 'no such request'))
            return

        request_name = requests[service]

        if request_name == 'ping':
            conn.write_message(create_pong())
            return
        elif request_name == 'roomlist':
            conn.write_message(create_roomlist(conn.possible_rooms))
            return

        data = get_data(message)

        logging.debug(data)

        if request_name == 'join':
            if conn.id.name != data['username']:                
                conn.id.change_name(data['username'])
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
        elif request_name == 'next_slide':
            room.send_message(create_next_slide())
        elif request_name == 'previous_slide':
            room.send_message(create_previous_slide())
        elif request_name == 'jump_to_slide':
            room.send_message(create_jump_to(data))