from django.db import models 

class Author(models.Model): 
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    date_of_birth = models.DateField() 

    def __str__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
