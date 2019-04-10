from django.contrib import admin

from . import models


@admin.register(models.Genre)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'name_slug')


@admin.register(models.Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('author', 'genre', 'title', 'description', 'text')
    list_filter = ('author', 'genre')
