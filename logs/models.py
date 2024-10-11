from django.db import models


class LogEvent(models.Model):
    timestamp = models.CharField(max_length=100)
    computer_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50)
    application = models.CharField(max_length=100)
    window_title = models.CharField(max_length=255)
    content = models.TextField()
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.event_type} on {self.computer_name}"
