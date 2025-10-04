from flask import jsonify, Blueprint

slash_route_blueprint = Blueprint("slash_route_bp", __name__)

@slash_route_blueprint.route("/", methods=["GET"])
def slash_route():
    return jsonify({
        "message": "Reservention API",
        "status": 200
    }), 200