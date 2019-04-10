from django.contrib import admin

from . import models


@admin.register(models.Card)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person', 'book', 'is_returned')
