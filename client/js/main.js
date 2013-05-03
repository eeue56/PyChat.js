$(document).ready(function () {
    var cs;

    Actions.message = function(name, message) {

    };
    Actions.pong = function() {
        
    };
    Actions.userList = function(users) {
        
    };
    Actions.roomList = function(rooms) {};
    Actions.userConnect = function(name) {};
    Actions.userDisconnect = function(name) {};
    Actions.nextSlide = function() {};
    Actions.previousSlide = function() {};
    Actions.jumpToSlide = function(number) {};


    $(".name").show();

    $(".modal .enter").click(function () {
        var userName = $("#name").val();

        // Create a chat session
        cs = new ChatSession({
            config: {
                url: "astraldynamics.co.uk",
                port: 80,
                resource: "ws"
            },
            user: new User({
                name: userName,
                avatar: ""
            })
        });

        // Get the list of rooms 
        // and display them for the user
        var roomReq = ServiceBuilder.build.roomList();
        cs.send(JSON.stringify(roomReq));
    });

});
