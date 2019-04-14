from django.db import models


class Card(models.Model):
    person = models.ForeignKey('users.Person', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    date_of_start = models.DateTimeField(verbose_name="Date when user took the book")
    date_of_end = models.DateTimeField(verbose_name="Date when user have to return the book.")
    is_returned = models.BooleanField(default=False)
    returning_date = models.DateTimeField(null=True)
