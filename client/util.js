arrayEach = function (a, callback) {
    for(var i = 0; i < a.length; i++) {
        callback(a[i], i);
    }
};
