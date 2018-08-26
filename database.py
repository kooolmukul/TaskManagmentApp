import sqlite3
def connect():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, taskName text, assignedTo text, status text, deadline TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP )")
    #cur.execute("DROP TABLE tasks")
    conn.commit()
    conn.close()

def insert(taskName, assignedTo, deadline,status='Pending'):
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks VALUES(NULL,?,?,?,?,datetime('now','localtime'))", (taskName,assignedTo,status,deadline) )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def delete(id):
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(taskName='', assignedTo='', status=''):
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE taskName=? OR assignedTo=? OR status=? ORDER BY created_at DESC",(taskName,assignedTo,status))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return rows

def update(id,taskName, assignedTo,deadline, status):
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET taskName=?, assignedTo=?,status=?, deadline=? ,created_at = datetime('now','localtime')  WHERE id=?",(taskName, assignedTo, status,deadline,id))
    conn.commit()
    conn.close()


connect()

#insert('Task1','Person1','2000-01-01 12:00 AM','Active')
#delete(5)
#search('Task1')
#update(4,'Task3','Mukul','Pending')
view()    