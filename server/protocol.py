from json import dumps, loads


requests = {0 : 'join',
            1 : 'ping',
            2 : 'send',
            3 : 'userlist',
            4 : 'roomlist'}

def create_message(username, message):
    return '{{"service":1, "data":{{"message":"{mes}", "username":"{user}"}} }}\n'.format(mes=message, user=username)

def create_pong():
    return '{"service" : 2}'

def create_userlist(usernames):
    return dumps({'service':3, 'data': {'users' : usernames}})

def create_roomlist(rooms):
    return dumps({'service':4, 'data': {'rooms' : rooms}})

def create_connect(username):
    return dumps({'service' : 5, 'data' : {'username' : username}})

def create_disconnect(username):
    return dumps({'service' : 6, 'data' : {'username' : username}})

def get_service(message):
    return loads(message)['service']

def get_data(message):
    return loads(message)['data']

services = {1 : create_message,
            2 : create_pong,
            3 : create_userlist,
            4 : create_roomlist,
            5 : create_connect,
            6 : create_disconnect}

def __test():
    assert loads(create_message('Noah', 'hi')) == {"service":1, "data":{"message":"hi", "username":"Noah"} }
    assert create_pong() == '{"service" : 2}'
    assert loads(create_userlist(['Harry'])) == {'service':3, 'data': {'users' : ["Harry"]}}


if __name__ == '__main__':
    __test()
