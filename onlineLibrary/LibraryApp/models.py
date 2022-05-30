from django.db import models


class Book(models.Model):
    publisher = models.CharField(max_length=20)
    namebook = models.CharField(max_length=30)
    description = models.TextField(help_text="Here is the description of the book")
    # pub_date = models.DateField(, help_text = "The is date publication")
    book = models.FileField(upload_to='books/pdf/')
    image = models.ImageField(upload_to='books/images/')

    def __str__(self):
        return self.publisher + " " + self.namebook
