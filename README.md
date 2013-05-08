PyChat.js
=========

PyChat.js is a chat client/server application using a Python backend (tornado) and a Javascript frontend, designed to be lightweight and extendable.
At the moment we're using websockets only - there is plans to enable the fallback ajax of graceful-websockets but it has not been done yet.
Because we use websockets, the performance of the server is very fast - almost instantiously. At the moment it doesn't support any version of Internet Explorer
Graceful-websockets it a little outdated for our use, and we will be looking into moving to a different provider for websocket support.



By default, PyChat.js listens on port 8000.

To set it up, either run the run_server.py file or have a file that contains
    import tornado.ioloop
    
    from pychatjs.server.run_server import application 
    
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
    
There is a sample chat client contained in the client folder. The actual server is in server. Database and configs contain samples of our setup.
We are using haproxy to send requests to Tornado and supervisord to keep the server alive.
