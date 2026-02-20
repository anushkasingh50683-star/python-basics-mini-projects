import sqlite3

DB_NAME = "students.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        create table if not exists students(
            id integer primary key autoincrement,
            name text not null,
            marks integer
                   ) 
    ''')
    conn.commit()
    conn.close()

def insert_data(name,marks):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        Insert into students (name,marks)Values(?,?)
    ''',(name,marks,))

    conn.commit()
    conn.close()

def view_all_data():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("Select * from students")

    rows = cursor.fetchall()
    conn.close()
     
    return rows
   
'''
cursor.execute() expects parameters as a sequence (tuple or list).
And tuples are created using commas.
The comma is what makes it a tuple.
When there is only one parameter then , is must otherwise its optional.
'''
    