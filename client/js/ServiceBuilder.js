var ServiceBuilder = {
    build: {
        join: function (username, room) {
            var json = {
                command: 0,
                data: {
                    username: username,
                    room: room
                }
            };
            return json;
        },

        ping: function (username) {
            var json = {
                command: 1,
                data: {
                    username: username
                }
            };
            return json;
        },

        message: function (username, message) {
            var json = {
                command: 2,
                data: {
                    username: username,
                    message: message
                }
            };
            return json;
        },    
    }
};
