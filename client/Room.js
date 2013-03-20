var ChatSession = Class.extend({
    init: function (settings) {
        this.id = settings.id; // the room object
        this.messages = settings.messages; // store messages
        this.users = settings.users; // array of users
        this.html = settings.html; // the location of the chat element
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
    }
});
