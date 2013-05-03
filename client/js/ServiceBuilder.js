var ServiceBuilder = {
    build: {
        join: function (username, room) {
            var json = {
                request: 0,
                data: {
                    username: username,
                    room: room
                }
            };
            return json;
        },

        ping: function (username) {
            var json = {
                request: 1,
                data: {
                    username: username
                }
            };
            return json;
        },

        message: function (username, message, room) {
            var json = {
                request: 2,
                data: {
                    username: username,
                    message: message,
                    room: room
                }
            };
            return json;
        },

        userList: function (room) {
            var json = {
                request: 3,
                data: {
                    room: room
                }
            };
            return json;
        }, 

        roomList: function (that) {
            var json = {
                request: 4
            };
            return json;
        },

        nextSlide: function () {
            var json = {
                request: 5,
            };
            return json;
        }, 

        previousSlide: function () {
            var json = {
                request: 6
            };
            return json;
        },  

        jumpToSlide: function (slideNumber) {
            var json = {
                request: 7,
                data: slideNumber
            };
            return json;
        }
    }
};
