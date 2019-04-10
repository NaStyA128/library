from django.db import models


class Genre(models.Model):
    name_slug = models.CharField(max_length=50)
    name = models.CharField(max_length=80, blank=True, null=True)


class Book(models.Model):
    author = models.ManyToManyField('users.Author', null=True)
    genre = models.ManyToManyField('books.Genre', null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    text = models.TextField()
    year = models.PositiveIntegerField(blank=True, null=True)
