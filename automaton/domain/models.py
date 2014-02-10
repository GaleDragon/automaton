from django.contrib.auth.models import User
from django.db import models
from oauth2client.django_orm import CredentialsField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^oauth2client\.django_orm\.CredentialsField"])

class Credential(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()