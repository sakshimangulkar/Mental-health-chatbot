import sqlite3

def fetch_emotions():
    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute("SELECT emotion FROM chats")
    data = cur.fetchall()

    conn.close()
    return [i[0] for i in data]