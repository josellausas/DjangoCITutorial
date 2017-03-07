# Hello world
import os

from django.test import Client
from django.test import TestCase

print('Hello Wolrd')

class SiteIsUpCase(TestCase):

    def setUp(self):
        self.client = Client()


    def test_site_is_up(self):
        # Get the index
        response = self.client.get('/')

        # Expect an OK
        self.assertEqual(response.status_code, 200)

        # Should have some html tags
        self.assertContains(response, '<html>')
