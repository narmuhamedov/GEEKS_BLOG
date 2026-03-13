from django.urls import path
from books.views import book_list_view, book_detail_view, search_view

app_name='knigi'

urlpatterns = [
    path('', book_list_view, name='books'),
    path('books_list/<int:id>/', book_detail_view),
    path('search/', search_view),
]