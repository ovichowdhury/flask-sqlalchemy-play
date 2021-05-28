import json
from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate
from db import db
from controllers.user_controller import user_controller


### init app ###
app = Flask(__name__, static_folder='static', static_url_path='/')
app.config.from_file('config.json', load=json.load)

### enable cors for app ###
CORS(app)

### init db ###
db.init_app(app)
Migrate(app, db)
with app.app_context():
    from models import *
    db.create_all()

### Global Exception Handler ###


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    payload = {
        "message": str(e)
    }
    return jsonify(payload), code


### registering all blueprints ###
app.register_blueprint(user_controller, url_prefix='/user')


### starting app ###
if __name__ == '__main__':
    app.run("0.0.0.0", 5000, threaded=True, debug=True)
