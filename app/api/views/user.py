# Standard library import
import re

# Thirdparty library imports
from passlib.hash import sha256_crypt
from flask_restful import Resource, reqparse
from flask import request, make_response, jsonify, session

# # Local application imports
# from app.api.utils.helpers.phone_verification import (phone_verification_check,
#                                                       phone_verification_start)

# models
from app.api.models.user import User

# schemas
from app.api.schemas.user_schema import UserSchema


class CreateAccount(Resource):
    """Create a new account."""

    def post(self):
        """Create an account for new user."""
        from app.api.utils.helpers.phone_verification import phone_verification_start, send_mail
        users = User.query.all()
        data = request.get_json(force=True)
        full_names = data["full_names"]
        email = data["email"]
        password = data["password"]
        user_type = data["user_type"]
        phone_number = data["phone_number"]
        country_code = data['country_code']

        current_user = [user for user in users if user.email ==
                        email or user.phone_number == phone_number]
        if current_user:
            # Bad request
            return make_response(
                jsonify({"message": "{} or {} Already Exist".format(
                    current_user[0].email, current_user[0].phone_number
                )}), 409)

        if not re.match(
            r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$',
                request.json['email']):
            # Bad request
            return make_response(jsonify({"message": "invalid Email"}), 400)

        if not re.match(
            '(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])',
                request.json['password']):
            # Bad request
            return make_response(jsonify({"message": "invalid password"}), 400)

        new_user_detail = {"user_id": len(users)+1,
                           "full_names": full_names,
                           "email": email,
                           "password": sha256_crypt.hash(password),
                           "user_type": user_type,
                           "phone_number": phone_number}
        schema = UserSchema()

        from flask_mail import Mail
        from instance.config import AppConfig
        from app import dramatiq, create_app

        app = create_app(AppConfig)
        mail = Mail(app)

        data1 = schema.load_object_into_schema(new_user_detail)
        new_data = User(**data1)
        new_data.save()
        # phone_verification_start(phone_number, country_code)
        send_mail.send()

        return make_response(
            jsonify({"message":
                     "Account created successfully"}), 201)  # created

        return make_response(jsonify(
            {"message": " {} Already Exist".format(
                request.json['email'])}), 409)  # conflict


class VerifyPhoneNumber(Resource):
    def post(self):
        from app.api.utils.helpers.phone_verification import phone_verification_check
        phone_verification_check.delay()
        verification.wait()
        phone_number = session.get("phone_number")
        cur_user = User.query.filter(
            User.phone_number == phone_number and not User.active).first()

        cur_user.active = True
        cur_user.save()

        if verification.ok():
            return make_response(
                jsonify({"message": "Phone number verified successfully"}))
        return make_response(
            jsonify({"message": "Failed to verify the Phone number"}), 201)
