from django.db import models
from custom_user.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    ISBN = models.PositiveBigIntegerField()
    published_date = models.DateField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class BookDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    book_id = models.OneToOneField(Book, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=225)
    language = models.CharField(max_length=225)

    def __str__(self):
        return f"BookID:{self.book_id} details"


class BorrowedBook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ManyToManyField(Book)
    borrow_date = models.DateField()
    return_date = models.DateField()
    return_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Borrow book {self.book_id} by user {self.user_id}"
