from django.db import models


class Card(models.Model):
    person = models.ForeignKey('users.Person', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    date_of_start = models.DateTimeField()
    date_of_end = models.DateTimeField()
    is_returned = models.BooleanField(default=False)
    returning_date = models.DateTimeField(null=True)
