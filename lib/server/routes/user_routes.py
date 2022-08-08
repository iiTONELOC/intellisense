from decouple import config
from flask import jsonify, request, make_response
from lib.server.middleware.auth import Auth
from lib.databases.models.user import User
from .utils import handle_response

USERS = config('USERS').split(',')

unauthorized_msg = {'unauthorized': {"message": 'Unauthorized'}}
def err_msg(msg): return {'error': {"message": f'{msg}'}}


def user_get(param=None):
    """User get route."""
    if param is None:  # 'api/users'
        return
    else:  # 'api/users/param'
        # get user by _id
        if Auth.is_authorized(request, param):
            user = User.get_user(param)
            return jsonify('mc.get_one_user(_id=param)')
        else:
            return make_response(jsonify(Auth.unauthorized_msg(None)), 401)


def user_post():
    """User post route."""
    # needs to be a tuple
    user_d = (v for k, v in request.json.items())
    username, password = user_d

    # check if the user can be created
    if username.strip() in USERS:
        #  we can create the user
        data = None
        try:
            # we need to hash the password
            hashed_pass = User.hash_password(password)
            user = User(username, hashed_pass)
            user = user.create_user()
            data = user
        except Exception as e:
            return handle_response(err_msg(str(e)))

        if data is not None:

            try:
                token = Auth.sign_token(
                    data['username'],
                    data['id']
                )
                return handle_response({
                    'token': token,
                    'username': data['username'],
                    "id": data['id']
                })
            except KeyError:
                return make_response(jsonify(data), 400)
            except TypeError as te:
                return make_response(jsonify('TypeError'), 400)
            except Exception as e:
                return make_response(jsonify({'error': e}), 500)
        else:
            return make_response(jsonify(data), 400)
    else:
        return handle_response(unauthorized_msg)


# def user_put(param=None):
#     """User put route."""
#     if param is None:  # 'api/users/param'
#         return
#     else:  # 'api/users/param'
#         # check if the request has the user object
#         if Auth.is_authorized(request, param):
#             data = mc.edit_user({
#                 "param": param,
#                 "body": request.json
#             })
#             if data is not None:
#                 return handle_response(data)
#             else:
#                 return None
#         else:
#             return make_response(jsonify(Auth.unauthorized_msg(None)), 401)


# def user_delete(param=None):
#     """User delete route."""
#     if param is None:  # 'api/users/param'
#         return
#     else:  # 'api/users/param'
#         if Auth.is_authorized(request, param):
#             data = mc.delete_user(param)
#             return handle_response(data)
#         else:
#             return make_response(jsonify(Auth.unauthorized_msg(None)), 401)


# # LOGIN/LOGOUT handlers
# # ----------------------


def user_login(data=None):
    """Login a user. returns a JWT token"""
    if data is None:
        return make_response(jsonify(err_msg('No data provided')), 400)
    else:
        match_user = None
        if 'username' in data:
            match_user = User().find_by_name(name=data['username'], pwd=True)
        # if match
        if match_user is not None:
            # user found now check password
            if User.check_password(data['password'], match_user['password']):
                # generate a token for the user
                try:
                    token = Auth.sign_token(
                        match_user['username'],
                        match_user['id']
                    )
                    return handle_response({
                        'token': token,
                        'username': match_user['username'],
                        "id": match_user['id']
                    })
                except TypeError as te:
                    return make_response(jsonify(err_msg(str(te))), 500)
                except Exception as e:
                    return make_response(jsonify(err_msg(str(e))), 500)
            else:
                return make_response(jsonify(err_msg('Not Found')), 404)
        else:
            return make_response(jsonify(err_msg('Not Found')), 404)
