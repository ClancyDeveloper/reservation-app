from flask import jsonify, Blueprint, request
from ...controllers.user.login_user_controller import login_user_controller

login_user_blueprint = Blueprint("login_user_blueprint", __name__)

@login_user_blueprint.route("/user/login", methods=["POST"])
def login_user():

    data = request.get_json()

    error = login_user_controller(data)

    if error:
        return jsonify({"error": error}), 401

    return jsonify({"message": "Login bem-sucedido"}), 200