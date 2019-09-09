# Local Application imports
from ..base_test import BaseTest

class TestCreateUsers(BaseTest):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
