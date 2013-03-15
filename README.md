PyChat.js
=========

PyChat.js is a chat client/server application using a Python backend (tornado) and a Javascript frontend, designed to be lightweight and extendable.


We are using nginx as a server with HAProxy in order to redirect connections to the websockets provided by Tornado. Supervisor is being used in order to manage tornado instances. The database engine is SQLite but this can easily be changed.
