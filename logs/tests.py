from django.test import TestCase
from .models import LogEvent
from django.urls import reverse


class LogEventTests(TestCase):

    def setUp(self):
        self.log = LogEvent.objects.create(
            computer_name="MacBook-Pro",
            event_type="Keyboard",
            application="PyCharm",
            window_title="Test Project",
            content="print('Hello, World!')"
        )

    def test_log_creation(self):
        log = LogEvent.objects.get(id=self.log.id)
        self.assertEqual(log.computer_name, "MacBook-Pro")

    def test_get_logs_api(self):
        response = self.client.get(reverse('get_logs'))
        self.assertEqual(response.status_code, 200)

    def test_create_log_api(self):
        data = {
            "computer_name": "Windows-PC",
            "event_type": "Mouse",
            "application": "Chrome",
            "window_title": "Google Search",
            "content": "Search query"
        }
        response = self.client.post(reverse('create_log'), data)
        self.assertEqual(response.status_code, 201)
