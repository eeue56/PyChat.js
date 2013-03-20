var ChatSession = Class.extend({
    init: function (settings) {
        this.messages = settings.messages; // store messages
        this.users = settings.users; // array of users
        this.html = settings.html; // the location of the chat element
        this.room = settings.room; // the room object
        this.me = settings.me;  // a reference to our own (authenticated) user.
    },
    addUser: function (user) {
        if(user) {
             this.users.push(user);
        } else {
             console.error(user, " is not a valid user object.");
        }
    },
    removeUser: function (userId) {
        for(var i = 0; i < this.users.length; i++) {
            if(this.users[i].user.id === userId) {
                 this.users.splice(i, 1);
            }
        }
    },
    send: function (data) {
        // send a message down the socket
        me.socket.send(data);
    },
    recieve: me.socket.onmessage = function (event) {
        var data = event.data;
        // do some shizzle with this data
    },
    ping: function () {
        
        me.socket.send(data);
    }
});
