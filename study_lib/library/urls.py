from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('add/', add_book, name='add_book'),
    path('add/', AddBook.as_view(), name='add_book'),
    # path('all_books/', all_books, name='all_books'),
    path('all_books/', BooksView.as_view(), name='all_books'),
    # path('book/<int:book_id>/', book_description, name='book_description'),
    path('book/<int:book_id>/', BookDetail.as_view(), name='book_description'),

    # path('test/', test),
]
