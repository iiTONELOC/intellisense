from flask import jsonify, make_response, request
from lib.server.routes.user_routes import *
from lib.server.controllers.remote_controller import *
from lib.server.middleware.auth import with_auth


def api_controller(name, BOT=None, param=None):
    auth = with_auth
    routes = {
        'users': {
            'POST': lambda: user_post(),
            # 'PUT': lambda: user_put(param),
            # 'GET': lambda: user_get(param),
            # 'DELETE': lambda: user_delete(param)
        },
        'remote': {
            'POST': lambda: auth(request, make_response, remote_access_API, BOT)
        },
        'deviceStatus': {'GET': lambda: auth(request, make_response, device_status_API, BOT)},
    }

    if name in routes:
        func = routes[name][request.method]
        return func()
    else:
        return make_response(jsonify({'message': 'Not Found'}), 404)
