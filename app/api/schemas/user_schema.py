# Third party imports
from marshmallow import fields, post_load, pre_load, Schema
from app.api.utils.validation_error import ValidationError

# Local application imports
from app.api.models.user import User
from .base_schema import BaseSchema


class UserSchema(BaseSchema):
    user_id = fields.Int()
    full_names = fields.Str()
    email = fields.Email()
    password = fields.Str()
    phone_number = fields.Str()
    active = fields.Boolean()
    user_type = fields.Str()
