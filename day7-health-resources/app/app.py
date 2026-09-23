from flask import Flask, jsonify
import os
import time
import socket

app = Flask(__name__)

START_TIME = time.time()

# Used for testing readiness
ready = True


@app.route("/")
def home():
    return jsonify({
        "application": "Kubernetes Day 7",
        "pod": socket.gethostname(),
        "message": "Application is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "alive",
        "pod": socket.gethostname()
    }), 200


@app.route("/ready")
def readiness():
    if ready:
        return jsonify({
            "status": "ready",
            "pod": socket.gethostname()
        }), 200

    return jsonify({
        "status": "not ready"
    }), 503


@app.route("/startup")
def startup():
    uptime = time.time() - START_TIME

    if uptime < 10:
        return jsonify({
            "status": "starting",
            "uptime": uptime
        }), 503

    return jsonify({
        "status": "started",
        "uptime": uptime
    }), 200


@app.route("/memory")
def memory():
    # Allocate approximately 100 MB for testing.
    data = bytearray(100 * 1024 * 1024)

    return jsonify({
        "status": "memory allocated",
        "size_mb": len(data) // (1024 * 1024)
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )

