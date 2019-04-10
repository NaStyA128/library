from django.contrib import admin

from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', 'additional_information')


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography')
    search_fields = ('user', 'biography', 'additional_information')
