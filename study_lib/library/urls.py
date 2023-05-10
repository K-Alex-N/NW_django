from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('all_books/', all_books, name='all_books'),
    path('book/<int:book_id>/', book_description, name='book_description'),
]
