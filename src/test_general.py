# Hello world
import os

from django.test import Client
from django.test import TestCase

from src import settings

print('Hello Wolrd')

class SiteCanRun(TestCase):

    def setUp(self):
        self.client = Client()

    def test_has_leads_app_installed(self):
        from src.apps import tasks
        self.assertIsNotNone(tasks)
        self.assertTrue('src.apps.tasks' in settings.INSTALLED_APPS)

    def test_has_tasks_app_installed(self):
        from src.apps import leads
        self.assertIsNotNone(leads)
        self.assertTrue('src.apps.leads' in settings.INSTALLED_APPS)

    def test_site_is_up_and_has_index(self):
        response = self.client.get('/')
        # Expect an OK
        self.assertEqual(response.status_code, 200)
        # Should have some html tags
        self.assertContains(response, '<html>')
