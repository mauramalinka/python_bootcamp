from django.db import models

class Author(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.imie}-{self.nazwisko}"

class Book(models.Model):
    title = models.CharField(max_length=200) #pierwsza kolumna
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to="books_covers/%Y/%m/%d")

    def __str__(self):
        return f"{self.title}-{self.author}"


# Create your models here.
