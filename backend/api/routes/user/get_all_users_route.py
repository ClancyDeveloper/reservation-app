from flask import jsonify, Blueprint
from ...controllers.user.get_all_users_controller import get_all_users_controller

from ...middlewares.users.no_users_found import no_users_found_middleware 


get_all_users_blueprint = Blueprint("get_all_users_blueprint", __name__)

@get_all_users_blueprint.route("/user", methods=["GET"])
def get_all_users():

    users_data = get_all_users_controller()

    no_users_error = no_users_found_middleware(users_data)

    if no_users_error:
        return jsonify({
            "message": no_users_error,
            "status": 404
        }), 404

    all_users = [{
        "id": user.id,
        "username": user.username,
        "password": user.password
    }  for user in users_data ] 
    

    return jsonify({
        "users": all_users,
        "status": 200
    }), 200
