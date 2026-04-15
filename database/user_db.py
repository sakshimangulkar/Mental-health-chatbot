import sqlite3

def create_user_table():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(u,p):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO users(username,password) VALUES(?,?)",(u,p))

    conn.commit()
    conn.close()


def login_user(u,p):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
    user = cur.fetchone()

    conn.close()
    return user