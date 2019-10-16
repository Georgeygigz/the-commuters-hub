# app file
# where initialization of the application takes place

# Standard library imports
import os


# Third party imports
from threading import local
from flask_mail import Mail
from flask_cors import CORS
from flask_restful import Api
from authy.api import AuthyApiClient

from flask import Flask, make_response, jsonify, Blueprint, render_template

# Local application imports
from app.api.models.databases import db
from instance.config import AppConfig, app_configuration
from app.api.views.user import CreateAccount, VerifyPhoneNumber
from app.api.models.user import User

# creating an instance of blueprint
blueprint = Blueprint('commuters', __name__, url_prefix='/api/v1')
app_api = Api(blueprint)


def create_app(config_name):
    # app configuration and initializations
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configuration[config_name])
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.secret_key = os.getenv('SECRET_KEY')

    # flask mail
    mail = Mail(app)
    mail.init_app(app)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'georgeymutti@gmail.com'
    app.config['MAIL_PASSWORD'] = 'GOD@3_12#A'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # register blueprints
    app.register_blueprint(blueprint)

    # initialize db
    db.init_app(app)

    # cross origin policy
    CORS(app)

    # registering new routes
    app_api.add_resource(VerifyPhoneNumber, '/auth/verify')
    app_api.add_resource(CreateAccount, '/auth/register')

    @app.route('/')
    def index():
        return render_template('vote.html')

    return app
