from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "backend",
        "message": "Hello from Flask backend",
        "pod": socket.gethostname()
    })


@app.route("/api")
def api():
    return jsonify({
        "service": "backend",
        "pod": socket.gethostname(),
        "message": "Request reached the backend successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "pod": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

