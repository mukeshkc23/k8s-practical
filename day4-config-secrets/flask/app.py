from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "application": os.getenv("APP_NAME", "Unknown"),
        "environment": os.getenv("ENVIRONMENT", "Unknown"),
        "log_level": os.getenv("LOG_LEVEL", "Unknown")
    })


@app.route("/config")
def config():

    return jsonify({
        "app_name": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "log_level": os.getenv("LOG_LEVEL")
    })


@app.route("/secret")
def secret():

    api_key = os.getenv("API_KEY")
    db_password = os.getenv("DB_PASSWORD")

    return jsonify({
        "api_key_configured": api_key is not None,
        "db_password_configured": db_password is not None
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
