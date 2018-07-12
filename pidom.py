from flask import Flask
from flask_restplus import Resource, Api, reqparse
from flask import request, Response, render_template
from functools import wraps

import gpio
import lightstate

import time

app = Flask(__name__, static_url_path='')
app.config.from_envvar('SETTINGS')
api = Api(app, default="domotica", doc='/doc')

from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

output = gpio.Output()
lightState = lightstate.LightState(app.config['REDIS_HOST'], app.config['REDIS_PORT'], app.config['REDIS_DB'], app.config['REDIS_PASSWORD'])

parser = reqparse.RequestParser()
parser.add_argument('action', type=str, default='up', choices=('up', 'down'))


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == app.config['USER'] and password == app.config['PASSWORD']

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

@api.route('/outside')
class Outside(Resource):
    @requires_auth
    def get(self):
        output.pulse(4)

@api.route('/stairs')
class Stairs(Resource):
    @requires_auth
    def get(self):
        output.pulse(5)

@api.route('/frontdoorgroupoff')
class FrontdoorGroupOff(Resource):
    @requires_auth
    def get(self):
        output.pulse(6)
@api.route('/frontdoorgroupon')
class FrontdoorGroupOn(Resource):
    @requires_auth
    def get(self):
        output.pulse(7)



if __name__ == '__main__':
    app.run(host='::')
