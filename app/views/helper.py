import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .users import user_by_username
#import jwt
from werkzeug.security import check_password_hash

from flask_jwt_extended import jwt_required, create_access_token, get_raw_jwt, get_jwt_identity



''' def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print('token recuperado:' + token)
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            print('secrete key q chegou...:' + app.config['SECRET_KEY'])
            print('vai tentar usar jwt.decode...:')
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print('passou... ')
            print('usuario: ' + data['username'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated '''


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate1': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user and check_password_hash(user.password, auth.password):
        #token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
        #                   app.config['SECRET_KEY'])
        #exp = datetime.datetime.now() + datetime.timedelta(hours=12)
        #print(f'data expiracao= {expiration}')
        token = create_access_token(identity = user.id)
        #token = create_access_token(identity = user.id, expires_delta = exp )
        return jsonify({'message': 'Validated successfully', 'token': token})
        #return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'),
        #                'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate2': 'Basic auth="Login required"'}), 401