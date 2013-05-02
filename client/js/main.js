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
    // do a test ping
    cs.requests.ping();
});
