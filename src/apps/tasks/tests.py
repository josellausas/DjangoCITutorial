from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from . import views


class TestTasks(TestCase):

    def setUp(self):
        self.client = Client()

    def test_task_index_is_ok(self):
        response = self.client.get(reverse(views.index))
        self.assertEqual(response.status_code, 200)

    def test_task_list_is_ok(self):
        # This URL's regex requires a single numeric argument
        response = self.client.get(reverse(views.detail, args=[0]))
        self.assertEqual(response.status_code, 200)
