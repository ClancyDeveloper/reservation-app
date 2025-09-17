from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from api.database import db
import os

from .routes.user.register_user_route import register_user_blueprint
from .routes.slash_route import slash_route_blueprint

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reservations.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(register_user_blueprint)
app.register_blueprint(slash_route_blueprint)

CORS(app, origins='*')


if __name__ == "__main__":
    app.run(debug=True)