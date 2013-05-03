from json import dumps, loads


REQUESTS = {0 : 'join',
            1 : 'ping',
            2 : 'send',
            3 : 'userlist',
            4 : 'roomlist',
            5 : 'next_slide',
            6 : 'previous_slide',
            7 : 'jump_to_slide'}

def create_message(username, message):
    """ Creates a standard message from a given user with the message """
    message = message.encode('string-escape')
    return '{{"service":1, "data":{{"message":"{mes}", "username":"{user}"}} }}'.format(
            mes=message, user=username)

def create_pong():
    """ Creates a pong """
    return '{"service" : 2}'

def create_userlist(usernames):
    """ Creates a userlist from usernames """
    return dumps({'service':3, 'data': {'users' : usernames}})

def create_roomlist(rooms):
    """ Creates a room list from rooms """
    return dumps({'service':4, 
                  'data': {'rooms' : [room.name for room in rooms]}
                  })

def create_connect(username):
    """ Connects a user """
    return dumps({'service' : 5, 'data' : {'username' : username}})

def create_disconnect(username):
    return dumps({'service' : 6, 'data' : {'username' : username}})

def create_next_slide():
    return dumps({'service' : 7})

def create_previous_slide():
    return dumps({'service' : 8})

def create_jump_to(slide_number):
    return dumps({'service' : 9, 'data' : slide_number})

def get_service(message):
    return loads(message)['request']

def get_data(message):
    return loads(message)['data']

def create_error(error_code, error_message):
    error_message = error_message.encode('string-escape')
    return dumps({ 'errors': [{'message' : error_message, 'code' : error_code}]})

services = {1 : create_message,
            2 : create_pong,
            3 : create_userlist,
            4 : create_roomlist,
            5 : create_connect,
            6 : create_disconnect,
            7 : create_next_slide,
            8 : create_previous_slide,
            9 : create_jump_to}

def __test():
    assert loads(create_message('Noah', 'hi')) == {"service":1, "data":{"message":"hi", "username":"Noah"} }
    assert create_pong() == '{"service" : 2}'
    assert loads(create_userlist(['Harry'])) == {'service':3, 'data': {'users' : ["Harry"]}}


if __name__ == '__main__':
    __test()
