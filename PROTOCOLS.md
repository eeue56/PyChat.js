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

### 7. Next slide
    {
        "service" : 7
    }

### 8. Previous slide
    {
        "service" : 8
    }

### 9. Jump to slide
    {
        "service" : 9,
        "data" : {
            "slide" : slide_number
        }
    }

### 10. User dump
    {
        "service" : 10,
        "data" : {
            user property name : user value
        }
    }

### 11. Users dump
    {
        "service" : 11,
        "data" : {
            user =[user property name : user value]
        }
    }

### 999. Error
    {
        "service" : 999,
        "data" : {
            "code" : error_code,
            "message" : "error_message"
        }
    }

    Error code:
                    1 - Request not found
                    2 - Username in use
                    3 - Username not found  


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

### 5. Next slide
    {
        "request" : 5
    }

### 6. Previous slide
    {
        "request" : 6
    }

### 7. Jump to slide
    {
        "request" : 7,
        "data" : {
            "slide" : slide_number
        }
    }
### 8. Get user dump
    {
        "request" : 8,
        "data" : {
            "name" : "user name"
        }
    }
### 9. Get users dump
    {
        "request" : 9,
        "data" : {
            "room" : "room_name"
        }
    }

### 10. Send user dump
    {
        "request" : 9,
        "data" : {
            "setting name" : "setting value"
        }
    }

### 112. Change name
    {
        "request" : 112,
        "data" : {
            "name" : "new name"
        }
    }