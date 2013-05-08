PyChat.js
=========

PyChat.js is a chat client/server application using a Python backend (tornado) and a Javascript frontend, designed to be lightweight and extendable.


By default, PyChat.js listens on port 8000.

To set it up, either run the run_server.py file or have a file that contains
    import tornado.ioloop
    
    from pychatjs.server.run_server import application 
    
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
    
There is a sample chat cl
