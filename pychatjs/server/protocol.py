from json import dumps, loads


requests = {0 : 'join',
            1 : 'ping',
            2 : 'send',
            3 : 'userlist',
            4 : 'roomlist',
            5 : 'next_slide',
            6 : 'previous_slide',
            7 : 'jump_to_slide',
            8 : 'get_user_dump',
            9 : 'get_users_dump',
            10 : 'send_dump',
            112 : 'change_name'}

def create_message(username, message):
    """ Creates a standard message from a given user with the message 
        Replaces newline with html break """
    message = message.replace('\n', '<br/>')
    return '{{"service":1, "data":{{"message":"{mes}", "username":"{user}"}} }}'.format(mes=message, user=username)

def create_pong():
    """ Creates a pong """
    return '{"service" : 2}'

def create_userlist(usernames):
    """ Creates a userlist from usernames """
    return dumps({'service':3, 'data': {'users' : usernames}})

def create_roomlist(rooms):
    """ Creates a room list from rooms """
    return dumps({'service':4, 'data': {'rooms' : [room.name for room in rooms]}})

def create_connect(username):
    """ Creates connect message for username """
    return dumps({'service' : 5, 'data' : {'username' : username}})

def create_disconnect(username):
    """ Creates disconnect message for username """
    return dumps({'service' : 6, 'data' : {'username' : username}})

def create_next_slide():
    """ Creates next slide """
    return dumps({'service' : 7})

def create_previous_slide():
    """ Creates previous slide """
    return dumps({'service' : 8})

def create_jump_to(slide_number):
    """ Creates a jump to given slide number """
    return dumps({'service' : 9, 'data' : {'slideNumber' : slide_number}})

def get_service(message):
    """ Gets the request from the message """
    return loads(message)['request']

def get_data(message):
    """ Gets the data payload from the message """
    return loads(message)['data']

def create_error(error_code, error_message):
    """ Creates an error with given code and message """
    error_message = error_message.replace('\n', '<br/>')
    return dumps({ 'service': 999, 'data' : {'message' : error_message, 'code' : error_code}})

def create_user_dump(user):
    return dumps({ 'service' : 10, 'data' : user._to_json()})

def create_users_dump(users):
    return dumps({ 'service' : 11, 'data' : [user._to_json() for user in users]})

services = {1 : create_message,
            2 : create_pong,
            3 : create_userlist,
            4 : create_roomlist,
            5 : create_connect,
            6 : create_disconnect,
            7 : create_next_slide,
            8 : create_previous_slide,
            9 : create_jump_to,
            10 : create_user_dump,
            11 : create_users_dump,
            999 : create_error}

def __test():
    assert loads(create_message('Noah', 'hi')) == {"service":1, "data":{"message":"hi", "username":"Noah"} }
    assert create_pong() == '{"service" : 2}'
    assert loads(create_userlist(['Harry'])) == {'service':3, 'data': {'users' : ["Harry"]}}


if __name__ == '__main__':
    __test()
