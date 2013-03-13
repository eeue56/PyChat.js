CREATE DATABASE IF NOT EXISTS Sockets;
USE Sockets;

CREATE TABLE IF NOT EXISTS Users
(
	username varchar(20),
	PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS Messages
(
	message_id INTEGER PRIMARY KEY AUTOINCREMENT,
	time_sent timestamp DEFAULT CURRENT_TIMESTAMP,
	username varchar(20),
	room_name varchar(20),
	FOREIGN KEY(room_name) REFERENCES Rooms(room_name),
	FOREIGN KEY(username) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS Rooms
(
	room_name varchar(20)
);
