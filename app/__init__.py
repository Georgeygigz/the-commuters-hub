# app file
# where initialization of the application takes place

# Standard library imports
import os
from dramatiq.brokers.redis import RedisBroker
import dramatiq

# Third party imports
from flask_mail import Mail
from flask_cors import CORS
from flask_restful import Api
from flask_redis import FlaskRedis
from authy.api import AuthyApiClient
from flask import Flask, make_response, jsonify, Blueprint
from threading import local

# Local application imports
from app.api.models.databases import db
from instance.config import AppConfig, app_configuration
from app.api.views.user import CreateAccount, VerifyPhoneNumber

# creating an instance of blueprint
blueprint = Blueprint('commuters', __name__, url_prefix='/api/v1')
app_api = Api(blueprint)


# class AppContextMiddleware(dramatiq.Middleware):
#     state = local()

#     def __init__(self, app):
#         self.app = app

#     def before_process_message(self, broker, message):
#         context = self.app.app_context()
#         context.push()

#         self.state.context = context

#     def after_process_message(self, exception=None, *args, **kwargs):
#         """
#         The keyword arguments (kwargs) are optional, any or none of the kwargs could be supplied
#         """
#         try:
#             context = self.state.context
#             context.pop(exception)
#             del self.state.context
#         except AttributeError:
#             pass

#     after_skip_message = after_process_message


def create_app(config_name):

    # app configuration and initializations
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configuration[config_name])
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.secret_key = os.getenv('SECRET_KEY')

    # dramtiq
    # redis_broker = RedisBroker(url='redis://localhost:6379/0')
    # redis_broker.add_middleware(AppContextMiddleware(app))
    # dramatiq.set_broker(redis_broker)

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
    def hello_world():
        return make_response(jsonify({"message": "Hello world"}))

    return app
