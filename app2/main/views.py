from flask import Flask, request, jsonify, Blueprint
main = Blueprint('main', __name__)
def all_users():
    user_list = [
    {'musoke':
            [{"user_id":1, 'password':'male'}]},

    {'ivan':
            [{"user_id":2, 'password':'password'}]},
    {'hassan':
            [{"user_id":3, 'password':'computer'}]},
    {'mary':
            [{"user_id":4, 'password':'mary'}]}
    ]
    return user_list

user_list = all_users()
@main.route('/api/user/add', methods = ['POST'])
def add_users():
    data = request.get_json()
    details = data.get('details')
    if details in user_list:
        return jsonify({"error": "User already added"}), 400
    user_list.append(details)
    return jsonify({'new_user': user_list}), 201

@main.route('/api/user/get', methods =['GET'])
def get_users():
    if len(user_list)==0:
        return jsonify({"message": "no learners available"}),404
    return jsonify ({"Users":user_list, "number":len(user_list)}),200

@main.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    details= data.get('details')
    if details in user_list:
        user_list.remove(details)
        return jsonify({'new_user': user_list}), 200
    return jsonify({"error":"user not found in the list "}), 400
