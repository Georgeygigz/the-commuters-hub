# Third party imports
from marshmallow import Schema


class BaseSchema(Schema):

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""

        data = self.load(data, partial=partial)
        if data:
            return data
        raise ValidationError(
            dict(errors=errors, message='An error occurred'), 400)
