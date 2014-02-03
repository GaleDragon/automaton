from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestRunner(models.Model):
    runner = models.ForeignKey(User)
    date_started = models.DateTimeField(auto_now_add=True)
    test_file = models.FileField(upload_to="tests/%Y/%m/%d")