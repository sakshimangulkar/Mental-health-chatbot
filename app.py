from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
import os
import io
import sqlite3
import matplotlib
matplotlib.use('Agg')   # Fix for deployment (no GUI)

import matplotlib.pyplot as plt

# Your custom modules
from model.predict import predict_emotion
from responses import get_response
from database.db import init_db, save_chat
from database.get_data import fetch_emotions
from database.user_db import create_user_table, register_user, login_user

app = Flask(__name__)
app.secret_key = "secretkey123"

# Initialize database
init_db()
create_user_table()

# ------------------ ROUTES ------------------ #

# Landing Page
@app.route("/")
def landing():
    return render_template("home.html")


# Signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        register_user(username, password)
        return redirect(url_for("login"))

    return render_template("signup.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            session["user"] = username
            return redirect(url_for("chatpage"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# Chat Page
@app.route("/chatpage")
def chatpage():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("chat.html", user=session["user"])


# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("landing"))


# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    emotion = predict_emotion(msg)
    reply = get_response(emotion)

    save_chat(msg, emotion)

    alert = ""
    if emotion in ["sad", "angry"]:
        alert = "⚠ Consider talking to someone you trust or a professional."

    return jsonify({
        "reply": reply,
        "emotion": emotion,
        "alert": alert
    })


# Emotion Graph
@app.route("/graph")
def graph():
    emotions = fetch_emotions()

    counts = {}
    for e in emotions:
        counts[e] = counts.get(e, 0) + 1

    plt.figure()
    plt.bar(counts.keys(), counts.values())

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')


# Chat History API
@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT message, emotion FROM chats WHERE user = ?",
        (session["user"],)
    )

    data = cur.fetchall()

    conn.close()

    return jsonify({"history": data})


# ------------------ RUN APP ------------------ #

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses dynamic port
    app.run(host="0.0.0.0", port=port)