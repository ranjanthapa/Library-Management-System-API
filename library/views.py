from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.response import Response
from .serializer import BookSerializer, BookDetailSerializer, BorrowBookSerializer
from .models import Book, BookDetail, BorrowedBook


class AddBook(CreateAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Added successfully"}, status.HTTP_201_CREATED)
        else:
            return Response({"error": "invalid data insertion"}, status.HTTP_400_BAD_REQUEST)


class ListOfBook(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RetrieveBook(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        book_detail_obj = self.get_object()
        serialize_data = BookDetailSerializer(book_detail_obj)
        return Response({"book_detail": serialize_data.data}, status.HTTP_200_OK)

    def get_object(self):
        book_detail_obj = get_object_or_404(BookDetail, book_id=self.kwargs.get('bookID'))
        return book_detail_obj


class UpdateBook(UpdateAPIView):
    serializer_class = BookDetailSerializer

    def update(self, request, *args, **kwargs):
        print(self.kwargs.get('detailID'))
        book_detail_obj = BookDetail.objects.get(detail_id=self.kwargs.get('detailID'))
        serialize_data = self.serializer_class(book_detail_obj, data=request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({"message": "updated successfully"}, status.HTTP_200_OK)

        else:
            return Response({"error": f"something went wrong {serialize_data.errors}"}, status.HTTP_400_BAD_REQUEST)


class BorrowBookView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serialize_data = BorrowBookSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({"message": "book borrowed successfully"}, status.HTTP_201_CREATED)
        else:
            return Response({"error": "something went bad"}, status.HTTP_400_BAD_REQUEST)


class ReturnBorrowBook(UpdateAPIView):

    def patch(self, request, *args, **kwargs):
        borrow_book_obj = get_object_or_404(BorrowedBook, pk=self.kwargs.get("borrow_id"))
        serialize_data = BorrowBookSerializer(borrow_book_obj, data=request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({"data": f"return successfully  {serialize_data.data}"}, status.HTTP_200_OK)
        else:
            return Response({"error": f"something went bad  {serialize_data.errors}"}, status.HTTP_400_BAD_REQUEST)


class ListOfBorrowBooks(ListAPIView):
    queryset = BorrowedBook.objects.filter(return_status=False)
    serializer_class = BorrowBookSerializer
