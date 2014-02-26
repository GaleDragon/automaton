from django.db import models
from django.contrib.auth.models import User
from django.dispatch import Signal

# Create your models here.
class TestProfile(models.Model):
    runner = models.ForeignKey(User)
    date_started = models.DateTimeField(auto_now_add=True)

class TestRunner(models.Model):
    test_run = models.ForeignKey(TestProfile)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    success = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=True)

