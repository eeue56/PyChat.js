import logging

from protocol import *


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

        if request_name == 'join':
            conn.join_room(data['user'])
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