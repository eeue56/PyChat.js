var Message = Class.extend({
    init: function (settings) {
        this.id = settings.id;
        this.user = settings.user;
        this.room = settings.room;
        this.body = settings.body || 
                    settings.text || 
                    settings.data;
        this.time = settings.time;
    },
    toHtml: function () {
        var html = $("<div></div>").attr("id", "m" + this.id);
        var time = $("<div></div>").attr("class", "time");
        var name = $("<span></span>").attr("class", "name");
        var body = $("<p></p>").attr("class", "message-body");
        
        time.html(this.time);
        name.html(this.user.name);
        body.html(this.body);

        $(body).prepend(name);
        $(html).append(time);
        $(html).append(body);
        return html;
    }
});
