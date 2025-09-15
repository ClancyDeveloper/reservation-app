from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)

CORS(app, origins='*')

@app.route("/")
def slash_route():
    return jsonify({
        "message": "reservation APP",
        "status": 200
    }), 200

print(f"Running on 127.0.0.1")

if __name__ == "__main__":
    app.run(debug=True)