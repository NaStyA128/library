from django.db import models


class Genre(models.Model):
    name_slug = models.CharField(max_length=50)
    name = models.CharField(max_length=80, blank=True)


class Book(models.Model):
    author = models.ManyToManyField('users.Author')
    genre = models.ManyToManyField('books.Genre')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    text = models.TextField()
    year = models.DateField(blank=True)
