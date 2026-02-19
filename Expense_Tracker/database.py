import sqlite3

def insert_expenses(category,desc,amt):
    conn = sqlite3.connect("expenses.db")

    c = conn.cursor()

    #c.execute('''
    #   Create table expenses(
    #         id integer primary key autoincrement,
    #          date text,
    #          category text,
    #          description text,
    #          amount real
    #          )
    #''')   

    c.execute('''
        Insert into expenses(date,category,description,amount) values(CURRENT_TIMESTAMP,?,?,?)
    ''',(category,desc,amt))         

    #c.execute("SELECT * FROM expenses")
    #rows = c.fetchall()

    #for row in rows:
    #   print(row)

    conn.commit()
    conn.close()
