import sqlite3
conn = sqlite3.connect("todo.db")
conn.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("INSERT INTO todo(task, status) VALUES ('Read A-byte-of-python to ', 'status 11')")
# conn.execute("INSERT INTO todo(task, status) VALUES ('REad A-bypte-of-python to ')")
# conn.execute("INSERT INTO todo(task, status) VALUES ('REad A-bypte-of-python to ')")
# conn.execute("INSERT INTO todo(task, status) VALUES ('REad A-bypte-of-python to ')")
conn.commit()