import sqlite3

if __name__ == "__main__":
  con = sqlite3.connect('example.db')
  with con:
  	con.executescript(open("databaseSetup.sql").read())


