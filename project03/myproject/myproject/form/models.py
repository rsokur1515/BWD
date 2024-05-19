from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    seat = models.PositiveSmallIntegerField(default=1, blank=False, null=False, choices=[(i, i) for i in range(1, 256)])

