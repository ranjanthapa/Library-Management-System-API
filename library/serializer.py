from rest_framework import serializers
from .models import Book, BookDetail, BorrowedBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ['user_id', ]


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['detail_id', 'book_id', 'number_of_pages', 'publisher', 'language']


class BorrowBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowedBook
        fields = ['user_id', 'book_id', 'borrow_date', 'return_date', 'return_status']

