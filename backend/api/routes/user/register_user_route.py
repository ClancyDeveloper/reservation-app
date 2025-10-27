from flask import jsonify, Blueprint, request

from ...controllers.user.register_user_controller import register_user_controller
from ...middlewares.users.duplicate_register_username import valid_username
from ...middlewares.users.validate_login_fields import validate_login_fields

register_user_blueprint = Blueprint("register_user_blueprint", __name__)

@register_user_blueprint.route("/user/register", methods=["POST"])
def register_user():

    data = request.json

    user = {
        "username": data.get("username"),
        "password": data.get("password")
        }

    valideate_fields_error = validate_login_fields(data)
    if valideate_fields_error:
        return jsonify({"error": valideate_fields_error}), 400

    validate_username_error = valid_username(user)
    if validate_username_error:
        return jsonify({"error": validate_username_error}), 400

    register_user_controller(user)

    return jsonify({"message": "User registered successfully"}), 201
