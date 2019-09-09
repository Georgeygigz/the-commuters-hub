# app file
# where initialization of the application takes place

# Standard library imports
import os

# Third party imports
from flask import Flask, make_response, jsonify
from flask_cors import CORS

# Local application imports
from instance.config import AppConfig, app_configuration
from app.api.models.databases import db

app = Flask(__name__)


def create_app(config_name):

    # app configuration and initializations
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configuration[config_name])
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")

    # initialize db
    db.init_app(app)

    # cross origin policy
    CORS(app)

    @app.route('/')
    def hello_world():
        return make_response(jsonify({"message": "Hello world"}))

    return app
