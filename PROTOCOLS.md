# Protocols #

## Server
### Services
#### 1. Message from user
    {
        "service":1,
        "data": {
            "message":"some message.",
            "username":"some_username"
        }
    }
#### 2. Pong
    {
        "service":2
    }
#### 3. Return Userlist
    {
        "service": 3,
        "data": {
            "users": [
                "username",
                ...
            ]
        }
    }
#### 4. Return RoomList
    {
        "service": 4,
        "data": {
            "rooms": [
                "roomId",
                ...
            ]
        }
    }
#### 5. User Connect
    {
        "service": 5,
        "data": {
            "username": "some_username"
        }
    }
#### 6. User Disconnect
    {
        "service": 6,
        "data": {
             "username": "some_username"
        }
    }

## Client
### Requests
#### 0. Join
    {
        "request":0,
        "data":{
            "username": "some_username",
            "room": "room_name"
        }
    }
#### 1. Ping
    {
        "request": 1
    }
#### 2. Send message
    {
        "request": 2,
        "data": {
            "username": "some_username",
            "room": "room_name_to_send_the_message_to",
            "message": "the users message."
        }
    }
#### 3. Get Userlist
    {
        "request": 3,
        "data" : { 
        	"room" : "room_name"
        }
    }
#### 4. Get RoomList
    {
        "request": 4
    }

### Errors
	1. Message not delivered
        	Error code:
            		0 - Room closed
    {
        "errors":[
            {
                "message":[reason]
                "code":[code]
            }
        ]
    }





