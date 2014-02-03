__author__ = 'jeremymorgan'

from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestRunner

@receiver(post_save, sender=TestRunner)
def start_runner(sender, **kwargs):
    if kwargs['created']:
        pass



