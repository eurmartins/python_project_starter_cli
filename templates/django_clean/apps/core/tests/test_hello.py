from django.test import TestCase
from django.urls import reverse

class HelloTestCase(TestCase):
    def test_hello_view(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello, World!'})