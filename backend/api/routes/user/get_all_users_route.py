from flask import jsonify, Blueprint
from ...controllers.user.get_all_users_controller import get_all_users_controller


get_all_users_blueprint = Blueprint("get_all_users_blueprint", __name__)

@get_all_users_blueprint.route("/user", methods=["GET"])
def get_all_users():

    users_data = get_all_users_controller()

    all_users = [{
        "id": user.id,
        "username": user.username,
        "password": user.password
    }  for user in users_data ] 
    

    return jsonify({
        "users": all_users,
        "status": 200
    }), 200
