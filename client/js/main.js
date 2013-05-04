$(document).ready(function () {
    window.cs = null;
    var pyjs = $("#pyjs");

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

        // set up a ping
        setInterval(function() {
            var ping = ServiceBuilder.build.ping();
            cs.send(JSON.stringify(ping));
        }, 20000);
    };

    /* MESSAGE ARRIVES */
    Services.message = function(name, message) {
        console.log("Service: Message");
        var msg = new Message({
            id: "0", // TODO: fix hardcoded ID
            user: name,
            body: message,
            time: util.currentTime()
        });

        var conversation = pyjs.find(".pyjs-conversation")[0];
        $(conversation).append(msg.toHtml());
        // autoscroll to bottom of chat
        conversation.scrollTop = conversation.scrollHeight;
    };

    /* PONG ARRIVES */
    Services.pong = function() {
        //console.log("Service: Pong");
        pyjs.find(".pyjs-ping").fadeIn(function() {
            pyjs.find(".pyjs-ping").fadeOut(1000);
        });
    };
    
    /* USERLIST RESPONSE ARRIVES */
    Services.userList = function(users) {
        console.log("Service: User List");
    };

    /* ROOMLIST RESPONSE ARRIVES */
    Services.roomList = function(rooms) {
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
            cs.room = roomName;

            pyjs.find(".pyjs-conversation-name").html(roomName);

            pyjs.removeClass("disabled");
            $(".rooms").fadeOut();
        });
    };

    /* A NEW USER CONNECTS */
    Services.userConnect = function(name) {
        console.log("Service: User Connect");
    };

    /* A USER DISCONNECTS */
    Services.userDisconnect = function(name) {
        console.log("Service: User Disconnect");
    };

    /* A NEXT SLIDE REQUEST */
    Services.nextSlide = function() {
        console.log("Service: Next Slide");
    };

    /* PREVIOUS SLIDE REQUEST */
    Services.previousSlide = function() {
        console.log("Service: PreviousSlide");
    };

    /* SLIDE JUMP REQUEST */
    Services.jumpToSlide = function(number) {
        console.log("Service: Jump Slide");
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

        var msgReq = ServiceBuilder.build.message(
            cs.user.name, msg, cs.room);

        cs.send(JSON.stringify(msgReq));
    });

});
