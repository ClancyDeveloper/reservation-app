from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from api.database import db
from model.client_model import Client
from model.reservation_model import Reservation
import os

# users routes
from .routes.user.register_user_route import register_user_blueprint
from .routes.user.get_all_users_route import get_all_users_blueprint
from .routes.user.login_user_route import login_user_blueprint

# client routes
from .routes.client.register_client_route import register_client_blueprint

from .routes.slash_route import slash_route_blueprint

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(register_user_blueprint)
app.register_blueprint(slash_route_blueprint)
app.register_blueprint(get_all_users_blueprint)
app.register_blueprint(login_user_blueprint)
app.register_blueprint(register_client_blueprint)

CORS(app, origins='*')

if __name__ == "__main__":   
    app.run(debug=True)