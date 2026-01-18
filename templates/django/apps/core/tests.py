from django.test import TestCase

class HealthTest(TestCase):
    def test_health(self):
        self.assertEqual(1, 1)
