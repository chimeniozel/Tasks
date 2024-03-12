from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    startDateTime = models.DateTimeField(null=True, blank=True)
    stopDateTime = models.DateTimeField(null=True, blank=True)  # Assuming this field represents the stop datetime

    def __str__(self):
        return self.title
