from flask import Flask, request, jsonify, Blueprint
from app2.main.models import GuestList
main = Blueprint('main', __name__)

guest = GuestList("", "",67, 4,"")
@main.route('/api/user/add', methods = ['POST'])
def add_users():
    all_users = guest.get_all_users()
    data = request.get_json()
    details = data.get('id')
    if details:
        guest.add_a_user(details, id)
        return jsonify({"message": all_users})
    return jsonify({"error":"not added"})


@main.route('/api/user/get', methods =['GET'])
def get_users():
    all_users = guest.get_all_users()
    # if len(user_list)==0:
    #     return jsonify({"message": "no learners available"}),404
    # return jsonify ({"Users":user_list, "number":len(user_list)}),200
    if all_users:
        return jsonify({"message": all_users}),200


@main.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    details= data.get('details')
    if details in user_list:
        user_list.remove(details)
        return jsonify({'new_user': user_list}), 200
    return jsonify({"error":"user not found in the list "}), 400
