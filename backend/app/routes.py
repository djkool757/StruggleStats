from flask import Blueprint, jsonify, request
from app.models import User, db, Topic, Category

## to get the page from jackwestin, 

api = Blueprint("api", __name__)

@api.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404