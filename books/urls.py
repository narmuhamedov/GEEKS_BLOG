from django.urls import path
from books.views import book_list_view, book_detail_view

urlpatterns = [
    path('books_list/', book_list_view),
    path('books_list/<int:id>/', book_detail_view),
]