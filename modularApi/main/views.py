from flask import Flask, request, jsonify, Blueprint
from modularApi.main.model import GuestList
main = Blueprint('main', __name__)

guest = GuestList()
@main.route('/api/user/add', methods = ['POST'])
def add_users():
    new = guest.add_a_user("kivumbi",2)
    return jsonify({'new_user': new}), 201

@main.route('/api/user/get', methods =['GET'])
def get_users():
    all_user = guest.get_all_users
    if not all_user:
        return jsonify({"message": "no learners available"}),404
    return jsonify ({"Users":all_user, "number":1}),200

@main.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    details= data.get('details')
    if details in user_list:
        user_list.remove(details)
        return jsonify({'new_user': user_list}), 200
    return jsonify({"error":"user not found in the list "}), 400
