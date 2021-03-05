import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(pitch = "Hello")

    def test_init(self):
        self.assertEqual(self.new_pitch.pitch,"Hello")