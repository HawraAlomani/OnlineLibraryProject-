from django.db import models
from LibraryApp.models import Book
from django.utils import timezone

'''
class ViewBook(models.Model):
    namebook = models.CharField(max_length=30, help_text="The is book name")
    book = models.ImageField(upload_to='pdf')

    def __str__(self):
        return self.namebook
'''

class Review(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, default="anonymous")
    comment = models.TextField(max_length=200)
    review_date = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
