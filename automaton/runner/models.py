from django.db import models
from django.contrib.auth.models import User
from django.dispatch import Signal

# Create your models here.
class TestRunner(models.Model):
    runner = models.ForeignKey(User)
    index = models.IntegerField()
    date_started = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    success = models.BooleanField(default=False)
    message = models.TextField()