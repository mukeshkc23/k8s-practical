from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "backend",
        "pod": socket.gethostname(),
        "message": "Backend reached through Ingress"
    })

@app.route("/api")
def api():
    return jsonify({
        "service": "backend",
        "pod": socket.gethostname(),
        "message": "API endpoint reached successfully"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

