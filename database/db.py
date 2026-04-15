import sqlite3

def init_db():
    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_chat(msg, emotion):
    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO chats(message,emotion) VALUES(?,?)",(msg,emotion))

    conn.commit()
    conn.close()