from django.db import models


class Card(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date_of_start = models.DateTimeField()
    date_of_end = models.DateTimeField()
    is_returned = models.BooleanField(default=False)
