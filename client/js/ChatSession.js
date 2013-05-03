/***
 *  ChatSession.js - Dan Prince
 * ---------------------------- 
 *  A chatSession is the global chat object 
 *  used by the user, which stores:
 *
 *  - The rooms the user is connected to
 *  - The user's web socket
 *  - The user object.
 *  
 *  It also contains wrapper methods for
 *  the socket's send & onmessage methods,
 *  in the forms of send and recieve.
 **/
var ChatSession = Class.extend({
    init: function (settings) {
        this.config = settings.config;
        this.user = settings.user;
        this.rooms = this.config.rooms || [];
        this.room = "";

        try { 
            // this is the websocket URL format
            // scheme://host:port/resource
            this.socket = $.gracefulWebSocket("ws://"
                + this.config.url +":"
                + this.config.port  +"/"
                + this.config.resource,
                {
                    fallbackPollParams: {
                         fallbackSendURL: "astraldynamics.co.uk/fws",
                         fallBackPollURL: "astraldynamics.co.uk/fws"
                    }
                });
        } catch (err) {
            console.error(err);
        }

        // bind the socket on message event
        // to the receive method.
        this.socket.onmessage = this.receive;
        this.socket.onerror = this.error;
        
        var self = this;    
        this.requests = {
            join: function () { 
                var json = ServiceBuilder.build.join();
                self.send(json);
            }, 
            ping: function () {
                var json = ServiceBuilder.build.ping(self.user.name);
                self.send(json); 
            },
            message: function () {
                var json = ServiceBuilder.build.message();
                self.send(json);
            },
            getUserList: function () {
                var json = ServiceBuilder.build.userlist();
                self.send(json);
            },
            getRoomList: function () {
                var json = ServiceBuilder.build.roomlist();
                self.send(json);
            },
            nextSlide : function () {
                var json = ServiceBuilder.build.nextSlide();
                self.send(json);
            },
            previousSlide : function () {
                var json = ServiceBuilder.build.previousSlide();
                self.send(json);
            },
            jumpToSlide : function () { 
                // TODO: replace hardcoded slidenumber with actual slide number
                var slideNumber = 5;
                var json = ServiceBuilder.build.jumpToSlide(slideNumber);
                self.send(json);
            },
        };
    },

    send: function (message) {
        whenReady(this.socket, 5000, function (socket) {
            socket.send(message); 
        });
    },
    receive: function (event) {
        // process data
        //console.log("We got data! " + event.data);
        
        try {
            var res = JSON.parse(event.data);
            var d = res.data;
        } catch(e) {
            console.error("Unrecognized Protocol");
            return false;
        }

        //console.log("SERVICE["+ res.service +"]");
        switch(res.service) {
            /* 1. Message from user */
            case 1:
                Actions.message(d.username, d.message);
                break;
            /* 2. Pong */
            case 2:
                Actions.pong();
                break;
            /* 3. Return Userlist */
            case 3:
                Actions.userList(d.users);
                break;
            /* 4. Return RoomList */
            case 4:
                Actions.roomList(d.rooms);
                break;
            /* 5. User Connect */
            case 5:
                Actions.userConnect(d.username);
                break;
            /* 6. User Disconnect */
            case 6:
                Actions.userDisconnect(d.username);
                break;
            /* 7. Next slide */
            case 7:
                Actions.nextSlide();
                break;
            /* 8. Previous slide */
            case 8:
                Actions.previousSlide();
                break;
            /* 9. Jump to slide */
            case 9:
                Actions.jumpToSlide(d.slideNumber);
                break;
            default:
                console.error("Unrecognized Protocol: " 
                    + res.service);
        }

    },
    error: function (event) {
        // process errors
        console.log("We got errors! " + event.data);
    },

    addRoom: function (room) {
        this.rooms.push(room);
    },
    removeRoom: function (roomId) {
       this.rooms.each(function (room, i) {
           if(room.id === roomId) {
               this.rooms.splice(i, 1);
           }
       }); 
    }
});
