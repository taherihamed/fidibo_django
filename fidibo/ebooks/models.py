from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=12, unique=True)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_rate = models.FloatField(max_length=3)
    book_price = models.CharField(max_length=15)
    book_translator = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)


