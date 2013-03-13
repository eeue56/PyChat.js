CREATE TABLE IF NOT EXISTS Users
(
	username varchar(20),
	PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS Messages
(
	messageID INTEGER PRIMARY KEY AUTOINCREMENT,
	sendTime timestamp DEFAULT CURRENT_TIMESTAMP,
	username varchar(20),
	roomName varchar(20),
	FOREIGN KEY(roomName) REFERENCES Rooms(roomName),
	FOREIGN KEY(username) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS Rooms
(
	roomName varchar(20)
);

/*
CREATE TABLE Meetings
(
	startTime datetime,
	endTime datetime,
	meetingName varchar(20),
	PRIMARY KEY(meetingName)
);

CREATE TABLE Attending
(
	meetingID varchar(20),
	username varchar(20),
	PRIMARY KEY(meetingID, username),
	FOREIGN KEY(meetingID) REFERENCES Meetings(meetingID),
	FOREIGN KEY(username) REFERENCES Users(username)
);
*/
