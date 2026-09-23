from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = "/data"
DATA_FILE = os.path.join(DATA_DIR, "messages.txt")


@app.route("/")
def home():
    return jsonify({
        "application": "Kubernetes Persistent Storage Demo",
        "storage_path": DATA_DIR
    })


@app.route("/write", methods=["POST"])
def write_data():

    message = request.json.get("message", "Default message")

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(DATA_FILE, "a") as file:
        file.write(
            f"{datetime.now()} - {message}\n"
        )

    return jsonify({
        "status": "success",
        "message": message
    })


@app.route("/read")
def read_data():

    if not os.path.exists(DATA_FILE):
        return jsonify({
            "status": "empty",
            "data": []
        })

    with open(DATA_FILE, "r") as file:
        data = file.readlines()

    return jsonify({
        "status": "success",
        "data": data
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )

