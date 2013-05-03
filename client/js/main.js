$(document).ready(function () {
    var cs;
    var pyjs = $("#pyjs");

    Actions.message = function(name, message) {
        console.log("Service: Message");
        console.log(message);
        var msg = new Message({
            id: "0", // TODO: fix hardcoded ID
            user: name,
            body: message,
            time: util.currentTime()
        });

        pyjs.find(".pyjs-conversation").html(msg.toHtml());
    };
    Actions.pong = function() {
        console.log("Service: Pong");
    };
    Actions.userList = function(users) {
        console.log("Service: User List");
    };

    Actions.roomList = function(rooms) {
        console.log("Service: Room List");
        // Show the rooms list
        $("#room-list").html(util.listBuilder(rooms, "join-room"));
        $(".rooms").removeClass("hidden");

        // Send a join request when the user clicks
        // one of the room names
        $(".join-room").click(function() {
            var roomName = $(this).html();
            var joinReq = ServiceBuilder.build.join(
                cs.user.name,
                roomName
            );
            cs.send(JSON.stringify(joinReq));

            pyjs.find(".pyjs-conversation-name").html(roomName);

            pyjs.removeClass("disabled");
            $(".rooms").fadeOut();
        });
    };

    Actions.userConnect = function(name) {
        console.log("Service: User Connect");
    };
    Actions.userDisconnect = function(name) {
        console.log("Service: User Disconnect");
    };
    Actions.nextSlide = function() {
        console.log("Service: Next Slide");
    };
    Actions.previousSlide = function() {
        console.log("Service: PreviousSlide");
    };
    Actions.jumpToSlide = function(number) {
        console.log("Service: Jump Slide");
    };

    var init = function(userName) {
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
    };

    $(".name").show();

    $(".enter").click(function () {
        var userName = $("#name").val();
        init(userName);
        $(".name").fadeOut();
    });

    pyjs.find(".pyjs-conversation-send").click(function() {
        var msg = pyjs.find(".pyjs-conversation-message").html();
        msg = msg.trim();
        // clear input
        pyjs.find(".pyjs-conversation-message").html("");
        var msgReq = ServiceBuilder.build.message(cs.user.name, msg);
        cs.send(JSON.stringify(msgReq));
    });

});
