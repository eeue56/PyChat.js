var Message = Class.extend({
    init: function (settings) {
        this.id = settings.id;
        this.user = settings.user;
        this.body = settings.body || 
                    settings.text || 
                    settings.data;
        this.time = settings.time;
    },
    toHtml: function (sameBlock) {
        var html = $("<div></div>").attr("id", "m" + this.id);
        var time = $("<div></div>").attr("class", "time");
        var name = $("<span></span>").attr("class", "name");
        var body = $("<p></p>").attr("class", "message-body");
        
        if(!sameBlock) {
            $(html).attr("class", "new-block");
            time.html(this.time);
            name.html(this.user);
            $(html).append(time);
            $(html).append(name);
        }

        body.html(this.body);
        $(html).append(body);
        return html;
    }
});
