import sqlite3

DB_NAME = "users.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    Create table if not exists users(
        id integer primary key autoincrement,
        name text not null
                   )
''')
    
    conn.commit()
    conn.close()

def insert_user(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("Insert into users (name) values(?)",(name,))
    
    conn.commit()
    conn.close()

