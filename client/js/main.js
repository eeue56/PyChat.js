$(document).ready(function () {
    cs = new ChatSession({
        config: {
            url: "astraldynamics.co.uk",
            port: 80,
            resource: "ws"
        },
        user: new User({
            name: "Dan",
            avatar: ""
        })
    });
    // send a ping every 20 seconds
    setInterval(20000, cs.requests.ping)
});
