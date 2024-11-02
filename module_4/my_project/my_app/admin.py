# admin.py
from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_birth')
    search_fields = ('name', 'email')
    list_filter = ('date_of_birth',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__name')  # Allows searching by author's name
    list_filter = ('published_date', 'author')  # Filter options based on publication date and author

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
