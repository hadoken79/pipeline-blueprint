import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "hello"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# @app.route("/user")
# def get_user():
#     username = request.args.get("username", "")
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     query = "SELECT * FROM users WHERE username = '" + username + "'"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify({"users": rows})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
