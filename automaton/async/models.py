from django.db import models
from runner.models import TestProfile

class Runner(models.Model):
    test_run = models.ForeignKey(TestProfile)
    done = models.BooleanField(default=False)
    success = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=True)
