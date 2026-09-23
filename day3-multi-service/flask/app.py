from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Flask Backend",
        "status": "running",
        "message": "Hello from Kubernetes Flask API"
    })


@app.route("/api")
def api():
    return jsonify({
        "service": "flask-service",
        "message": "Request successfully reached Flask backend"
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

