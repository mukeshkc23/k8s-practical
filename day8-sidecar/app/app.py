from flask import Flask, jsonify
import os
from datetime import datetime
import socket

app = Flask(__name__)

LOG_DIR = "/shared"
LOG_FILE = os.path.join(LOG_DIR, "application.log")


def write_log(message):

    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(
            f"{datetime.now()} "
            f"[{socket.gethostname()}] "
            f"{message}\n"
        )


@app.route("/")
def home():

    write_log("Home endpoint accessed")

    return jsonify({
        "application": "Day 8 Sidecar Application",
        "pod": socket.gethostname(),
        "message": "Flask application is running"
    })


@app.route("/api")
def api():

    write_log("API endpoint accessed")

    return jsonify({
        "service": "flask",
        "pod": socket.gethostname(),
        "message": "API request successful"
    })


@app.route("/health")
def health():

    write_log("Health endpoint checked")

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    write_log("Flask application started")

    app.run(
        host="0.0.0.0",
        port=5000
    )
