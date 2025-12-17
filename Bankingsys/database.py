import sqlite3

def get_connection():
    return sqlite3.connect("bank.db", check_same_thread=False)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS account (
        accno INTEGER PRIMARY KEY,
        name TEXT,
        balance INTEGER

    )      
               
    """)
    conn.commit()
    conn.close()