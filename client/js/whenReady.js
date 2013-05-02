/*
 * whenReady.js - Dan Prince
 */

/*
 * Checks whether a socket is ready for
 * message sending yet.
 * 
 * Ready States
 * 0 - Connecting
 * 1 - Open
 * 2 - Closing
 * 3 - Closed
 *
 */
var whenReady = function (socket, timeout, callback) {
    var interval = 100;
    Debug.out("Is socket ready...?");
    Debug.out("State: " + socket.readyState);
    switch(socket.readyState) {
        case 0: // connecting 
            if((timeout -= interval) <= 0) {
                return false;
            } else {
                setTimeout(function () {
                    whenReady(socket, timeout, callback);
                }, interval);
            }
            break;
        case 1: // open
            callback(socket);
            return true;
            break;
        case 2: // closing
            console.error("Could not send. Socket is closing.");
            return false;
            break;
        default: // closed
            console.error("Could not send. Socket is closed.");
            return false;
    } 
};
