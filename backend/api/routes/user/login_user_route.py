from flask import jsonify, Blueprint, request

from ...controllers.user.login_user_controller import login_user_controller

from ...middlewares.users.validate_login_fields import validate_login_fields
from ...middlewares.users.validate_login_user import validate_login_user

login_user_blueprint = Blueprint("login_user_blueprint", __name__)

@login_user_blueprint.route("/user/login", methods=["POST"])
def login_user():

    data = request.get_json()

    validate_login_fields_error = validate_login_fields(data)

    validate_login_user_error = validate_login_user(data)


    if validate_login_fields_error:
        return jsonify({
            "error": validate_login_fields_error
        }), 400

    if validate_login_user_error:
        return jsonify({
            "error": validate_login_user_error
        }), 401

    login_user = login_user_controller(data)
    return jsonify({"message": "Login bem-sucedido"}), 200