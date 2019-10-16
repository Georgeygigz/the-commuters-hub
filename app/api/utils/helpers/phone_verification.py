# app/api/utils/helpers/phone_verification.py

# Standard library imports
import os

# Thirdparty library imports
from flask_mail import Mail
from flask_mail import Message
from authy.api import AuthyApiClient
from flask import request, make_response, jsonify, session


# Local application imports
from instance.config import AppConfig
from app import create_app

app = create_app(AppConfig)
mail = Mail(app)
authy_api = AuthyApiClient(os.getenv('PRODUCTION_API_KEY'))


def phone_verification_start(phone_number, country_code):
    print('<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')
    print('>>>>>>>>>>>>>>>>>', phone_number, country_code)
    print('<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')

    try:
        session['country_code'] = country_code
        session['phone_number'] = phone_number
        authy_api.phones.verification_start(
            phone_number, country_code, via='sms')
        return True
    except Exception as e:
        return {'error': e}


def phone_verification_check():
    try:
        request_payload = request.get_json(force=True)
        verification_code = request_payload['code']
        phone_number = session.get("phone_number")
        country_code = session.get("country_code")
        verification = authy_api.phones.verification_check(
            phone_number,
            country_code,
            verification_code)
        return verification
    except Exception as e:
        return {'error': e}


def send_mail():
    try:
        message = Message("Hello",
                          sender="georgeymutti@gmail.com",
                          recipients=["george.mutti@andela.com"])
        mail.send(message)
        print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>')
        print('<<<<<<<<<<<<<<<', message, '>>>>>>>>>>>>>>>>>>')
        print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>')

        return True

    except Exception as e:
        return {"message": e}
