from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Kubernetes Day 2 🚀</h1>
    <h2>Flask Application</h2>
    <p>Application successfully deployed on Kubernetes!</p>
    """

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)