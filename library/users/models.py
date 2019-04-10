from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_information = models.TextField(blank=True, null=True)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
