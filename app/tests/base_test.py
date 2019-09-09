# Standard library imports
import json
import unittest

# Third party Library imports
# Local Application imports
from instance.config import AppConfig
from app import create_app
from app.api.models.databases import db
from app.api.models.user import User


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.app.testing = True

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

