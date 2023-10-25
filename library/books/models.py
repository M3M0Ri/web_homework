from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return f'({self.first_name} - {self.last_name})'


class Shelf(models.Model):
    number = models.IntegerField()
    corridor = models.CharField(max_length=100)

    def __str__(self):
        return f'Shelf Number : {self.number}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13)
    language = models.CharField(max_length=200)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return (f"title: {self.title} , author: {self.author} in "
                f"{self.publication_year} ")

