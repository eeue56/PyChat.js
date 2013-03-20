var Chat = {
    user: null,
    url: "astraldynamics.co.uk",
    port: 8080,
    setup: function (user) {
         this.user = user;
    },
    connect: function () {
        this.user.socket = $.gracefulWebSocket("ws://"+ this.url
            +":"+ this.port  +"/");
        
        // send the join request
        var req = ServiceBuilder.build.join(this.user.id);
        this.user.socket.send(req);
        // now the request has gone
        // we have to wait for our
        // response in the socket
        // onmessage method.
    }


}
