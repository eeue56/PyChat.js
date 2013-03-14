var ChatSession = Class.extend({
    init: function (settings) {
        this.id = settings.id;
        this.messages = settings.messages;
        this.users = settings.users;
        this.html = settings.html;
    };
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
        
});
