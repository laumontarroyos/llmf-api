from app import app
from flask import jsonify, url_for, redirect
from ..views import users, helper
from flask_jwt_extended import jwt_required, get_current_user, get_jwt_identity


"""Neste arquivo iremos criar todas rotas para aplicação para manter o código limpo usando
 as views(controllers)  e as relacionando por meio de funções"""


#@app.route('/', methods=['GET'])
#@helper.token_required
#def root(current_user):
#    return jsonify({'message': f'Oi {current_user.name}'})
#def root():
#    return jsonify({'message': f'Oi laureano!'})


@app.route('/', methods=['GET'])
#@helper.token_required
@jwt_required
def root():
    #current_user = get_jwt_identity()
    #return jsonify({'message': f'Hello {(users.get_user(get_jwt_identity())).name}'})
    return jsonify({'message': f'Hello {current_user.name}'})


@app.route('/authenticate', methods=['POST'])
def authenticate():
    return helper.auth()


@app.route('/users', methods=['GET'])
def get_users():
    return users.get_users()


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)


@app.route('/users', methods=['POST'])
def post_users():
    return users.post_user()

@jwt_required
@app.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    return users.delete_user(id)

@jwt_required
@app.route('/users/<id>', methods=['PUT'])
def update_users(id):
    return users.update_user(id)

#@app.route('/v1/auth', methods=['POST'])
#def auth():
#    pass