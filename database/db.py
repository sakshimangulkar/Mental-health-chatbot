import sqlite3

def init_db():
    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        emotion TEXT,
        user TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_chat(message, emotion, user):
    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO chats (message, emotion, user) VALUES (?, ?, ?)",
                (message, emotion, user))

    conn.commit()
    conn.close()