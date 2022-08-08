import os
from lib.alfred.alfred import Alfred
from lib.databases.models.user import User
from lib.server.routes.user_routes import user_login, user_post
from lib.server.controllers.api_route_controller import api_controller
from flask import Flask, request, make_response, render_template, send_from_directory

static = './lib/ui/web/build/'
static = os.path.normpath(static)
app = Flask(__name__, static_url_path='',
            static_folder=static,
            template_folder=static,)

BOT = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/<name>")
def react(name):
    if name in os.listdir(static):
        try:
            return send_from_directory(static, name)
        except FileNotFoundError:
            return make_response(f"{name} not found", 404)
    else:
        return render_template('index.html')


@app.route('/users/<name>/dashboard')
def user_dash(name):
    # look up user in db
    if User().find_by_id(id=name) is not None:
        return render_template('index.html')
    else:
        # FIXME redirect to the not found page
        return make_response(f"User not found", 404)


@app.route('/api/<name>', methods=['GET', 'POST'])
def api(name):
    global BOT

    # add auth to all the api routes?
    return api_controller(name, BOT)


@app.route('/api/users/<name>',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_1(name):
    if name == 'login':
        return user_login(request.json)
    return api_controller('users', None)


def start_server():
    # Build Front-End
    os.system('cd lib/ui/web && npm run build && cd..')
    # Initialize Alfred, but do not run Alfred
    # We can still use Alfred's functionality without running it
    global BOT
    BOT = Alfred()
    # start the server
    app.run(debug=False, port=5000, host='0.0.0.0')


if __name__ == "__main__":
    start_server()
