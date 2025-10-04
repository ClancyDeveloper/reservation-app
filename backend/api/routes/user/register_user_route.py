from flask import jsonify, Blueprint, request

from ...controllers.user.register_user_controller import register_user_controller

register_user_blueprint = Blueprint("register_user_blueprint", __name__)

@register_user_blueprint.route("/user/register", methods=["POST"])
def register_user():

    data = request.json

    error = register_user_controller(data)

    if error:
        return jsonify({
            "status": 400,
            "message": error
        }), 400

    return jsonify({
        "message": "Usuario registrado com sucesso",
        "status": 200
    }), 200

    