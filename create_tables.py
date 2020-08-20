import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"  # real = number with decimal
cursor.execute(create_table_items)

#cursor.execute("INSERT INTO items VALUES ('test', 23.88)")  # this is no need if we add post method in database function

connection.commit()

connection.close()
