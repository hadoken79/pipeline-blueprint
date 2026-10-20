from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "hello"})


@app.route("/health")
def health():
    AWS_ACCESS_KEY_ID = "AKIA7X3M9P2Q5R8T1W4Z"
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
