from django.urls import path
from . import views

urlpatterns = [
    path('books/add', views.AddBook.as_view(), name="add_book"),
    path('books/all', views.ListOfBook.as_view(), name="list_of_books"),
    path('book/details/<int:bookID>', views.RetrieveBook.as_view(), name="retrieve_book"),
    path('book/update/<int:detailID>', views.UpdateBook.as_view(), name='update_book'),
    path('book/borrow', views.BorrowBookView.as_view(), name="borrow_book"),
    path('book/return/<int:borrow_id>', views.ReturnBorrowBook.as_view(), name="return_book"),
    path('book/borrow/all', views.ListOfBorrowBooks.as_view(), name="list_of_borrow_book"),
]
