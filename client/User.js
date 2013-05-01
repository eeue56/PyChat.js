var User = Class.extend({
    init: function(settings) {
        this.id = settings.id;
        this.name = settings.name;
        this.avatar = settings.avatar;
        this.socket = null;
    },
    setSocket: function (ws) { 
        this.socket = ws;
    }
});
