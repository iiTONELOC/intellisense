from flask import jsonify

import jwt
from decouple import config
from datetime import datetime, timedelta


def set_expiration():
    return (datetime.now() + timedelta(days=90)).timestamp()


def get_secret_keys():
    return {
        'SECRET_KEY': config('SECRET_KEY'),
    }


class Auth:
    @staticmethod
    def sign_token(username, id):
        keys = get_secret_keys()
        payload = {
            'username': username,
            'id': id
        }
        return jwt.encode(payload, keys['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def get_token(req):
        if req.headers.get('Authorization'):
            try:
                return req.headers.get('Authorization').split(' ')[1].strip()
            except IndexError as e:
                return {'error': {'message': f'Invalid token: {e}'}}
        else:
            return None

    @staticmethod
    def decode_token(token):
        keys = get_secret_keys()
        try:
            return jwt.decode(token, keys['SECRET_KEY'], algorithms=['HS256'])
        except jwt.exceptions.ExpiredSignatureError:
            return Auth.unauthorized_msg(None)
        except jwt.exceptions.InvalidSignatureError:
            # FIXME
            # create a tracker that tracks the ip and number of failed attempts
            # if the number of failed attempts is greater than 5, block the ip
            return Auth.unauthorized_msg('Invalid token. Please log in again.')
        except jwt.exceptions.DecodeError as e:
            return Auth.unauthorized_msg(e)

    @staticmethod
    def is_authorized(req, id):
        """Checks the id of the auth token against the id of the user"""
        token = Auth.get_token(req)

        if token is not None:
            decoded = Auth.decode_token(token)
            if 'Unauthorized' in decoded:
                return False
            else:
                if decoded['id'] == id:
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def is_logged_in(req):
        token = Auth.get_token(req)
        if token is not None:
            decoded = Auth.decode_token(token)
            if 'Unauthorized' in decoded:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    def unauthorized_msg(msg):
        return {'Unauthorized': {
            'message': f'{msg or "Session expired. Please log in again."}'
        }}


def with_auth(req, res, next, app=None):
    token = Auth.get_token(req)
    if token is not None:
        decoded = Auth.decode_token(token)
        if 'Unauthorized' in decoded:
            return res(
                jsonify(
                    Auth.unauthorized_msg(
                        'Please log in to access this resource.'
                    )), 401)
        else:
            return next(req, res, app)
    else:
        return res(
            jsonify(
                Auth.unauthorized_msg(
                    'Please log in to access this resource.'
                )), 401
        )
