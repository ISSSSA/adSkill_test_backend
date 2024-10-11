from django.db import models

from django.utils import timezone


class LogEvent(models.Model):
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    computer_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50)
    application = models.CharField(max_length=255)
    window_title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.timestamp} - {self.event_type} on {self.computer_name}"
