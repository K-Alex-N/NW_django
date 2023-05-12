from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', BookCreate.as_view(), name='add_book'),
    path('all_books/', BookList.as_view(), name='all_books'),
    path('book/<int:book_id>/', BookDetail.as_view(), name='book_description'),

    # path('test/', test),
]
