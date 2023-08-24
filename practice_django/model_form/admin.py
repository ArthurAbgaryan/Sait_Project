from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','title','birth_day']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['name','authors']
    list_display = ['name','get_authors']


# Register your models here.
