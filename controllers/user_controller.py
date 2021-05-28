from flask import Blueprint, request, jsonify, abort, g


### init blueprint ###
user_controller = Blueprint('user_controller' , __name__)


from services.user_service import create_user, delete_user, get_user, update_user

### Dummy Data ###
user = []

@user_controller.get('/')
def get():
    users = get_user()
    return jsonify(users), 200

@user_controller.post('/')
def post():
    data = request.get_json()
    u = create_user(data)
    return jsonify({'id': u.id}), 201

@user_controller.put('/<id>')
def put(id):
    data = request.get_json()
    update_user(id, data)
    return jsonify({id: id}), 200

@user_controller.delete('/<id>')
def delete(id):
    delete_user(id)
    return jsonify({'id': id}), 200