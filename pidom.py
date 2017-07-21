from flask import Flask
from flask_restplus import Resource, Api, reqparse
from flask import request, Response, render_template
from functools import wraps

import gpio
import time

app = Flask(__name__, static_url_path='')

app.config.from_object('settings')

api = Api(app, default="domotica", doc='/doc')

output = gpio.Output()

parser = reqparse.RequestParser()
parser.add_argument('action', type=str, default='up', choices=('up', 'down'))


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == app.config['AUTH_USER'] and password == app.config['AUTH_PASS']

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
### END Basic Auth



@requires_auth
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')



@api.route('/screen')
class Screen(Resource):
    @requires_auth
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        print args
        if args['action'] == "down":
            output.pulse(1)
        elif args['action'] == 'up':
            output.pulse(2)

@api.route('/garage')
class Garage(Resource):
    @requires_auth
    def get(self):
        output.pulse(0,1)



@api.route('/alloff')
class Alloff(Resource):
    @requires_auth
    def get(self):
        output.pulse(3)

if __name__ == '__main__':
    app.run(host='::')
