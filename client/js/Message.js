var Message = Class.extend({
    init: function (settings) {
        this.id = settings.id;
        this.user = settings.user;
        this.body = settings.body || 
                    settings.text || 
                    settings.data;
        this.time = settings.time;
    },
    toHtml: function () {
        var html = $("<div></div>").attr("id", "m" + this.id);
        var time = $("<div></div>").attr("class", "time");
        var name = $("<span></span>").attr("class", "name");
        var body = $("<pre></pre>").attr("class", "message-body");
        
        time.html(this.time);
        name.html(this.user);
        body.html(this.body);

        $(html).append(time);
        $(html).append(name);
        $(html).append(body);
        return html;
    }
});
