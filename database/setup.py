import sqlite3

if __name__ == "__main__":
  connection = sqlite3.connect('example.db')
  c = connection.cursor()
  script = open("databaseSetup.sql").read()
  c.executescript(script)
  connection.commit()
  connection.close()


