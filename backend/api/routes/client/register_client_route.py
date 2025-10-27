from flask import jsonify, Blueprint, request

from ...controllers.client.register_client_controller import client_register_controller

register_client_blueprint = Blueprint("register_client_route_blueprint", __name__)

@register_client_blueprint.route("/client/register", methods=["POST"])
def register_client_route():
    data = request.json

    new_client = {
        "name": data.get("name"),
        "cpf": data.get("cpf"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "user_id": data.get("user_id")
    }

    client_register_controller(data)

    return jsonify({"message": "Sucesso"})



