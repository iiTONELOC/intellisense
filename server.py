import os
from lib.alfred.alfred import Alfred
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


def start_server():
    global BOT

    # Build Front-End
    os.system('cd lib/ui/web && npm run build && cd..')
    # Initialize Alfred, but do not run Alfred
    # We can still use Alfred's functionality without running it
    BOT = Alfred()
    # start the server
    app.run(debug=True, port=5000, host='0.0.0.0')


if __name__ == "__main__":
    start_server()
