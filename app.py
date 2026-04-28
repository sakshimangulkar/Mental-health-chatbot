from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import sqlite3

from model.predict import predict_emotion
from responses import get_response
from database.db import init_db, save_chat
from database.user_db import create_user_table, register_user, login_user

app = Flask(__name__)
app.secret_key = "secretkey123"

init_db()
create_user_table()

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        register_user(u, p)
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        user = login_user(u, p)

        if user:
            session["user"] = u
            return redirect(url_for("chatpage"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/chatpage")
def chatpage():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("chat.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    print("Message received:", msg)

    emotion = predict_emotion(msg)
    reply = get_response(emotion)

    save_chat(msg, emotion, session["user"])

    return jsonify({
        "reply": reply
    })
@app.route("/history")
def history():
    if "user" not in session:
        return jsonify({"history": []})

    conn = sqlite3.connect("database/chat.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT message, emotion FROM chats WHERE user=?",
        (session["user"],)
    )

    data = cur.fetchall()
    conn.close()

    return jsonify({"history": data})

if __name__ == "__main__":
    app.run(debug=True, port=10000)