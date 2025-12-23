from database import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENTS(
        stdId INTEGER PRIMARY KEY,
        name TEXT,
        contact TEXT,
        branch TEXT,
        year INTEGER
    )            
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        bookId INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        available INTEGER DEFAULT 1
    )        
    """)

    conn.commit()
    conn.close()
