import unittest
from app.models import Role

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_role = Role(name = "Admin")

    def test_init(self):
        self.assertEqual(self.new_role.name,"Admin")