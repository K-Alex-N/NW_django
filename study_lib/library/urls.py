from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('book/list/',                  BookList.as_view(), name='all_books'),
    path('book/<int:book_id>/',         BookDetail.as_view(), name='book_description'),
    path('book/add/',                   BookCreate.as_view(), name='book_create'),
    path('book/update/<int:book_id>/',  BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:book_id>/',  BookDelete.as_view(), name='book_delete'),

    path('author/list/',                    AuthorList.as_view(), name='author_list'),
    path('author/<int:book_id>/',           AuthorDetail.as_view(), name='author_detail'),
    path('author/add/',                     AuthorCreate.as_view(), name='author_create'),
    path('author/update/<int:book_id>/',    AuthorUpdate.as_view(), name='author_update'),
    path('author/delete/<int:book_id>/',    AuthorDelete.as_view(), name='author_delete'),


    # path('test/', test),
]
