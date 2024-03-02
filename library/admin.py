from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookDetail)
admin.site.register(BorrowedBook)