# books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    summary = models.CharField(max_length=255, blank=True)  # New field

    def __str__(self):
        return self.title
