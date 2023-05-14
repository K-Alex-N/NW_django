from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('feedback/', feedback, name='feedback'),

    path('book/list/',             BookList.as_view(), name='book_list'),
    path('book/<int:id>/',         BookDetail.as_view(), name='book_detail'),
    path('book/add/',              BookCreate.as_view(), name='book_create'),
    path('book/update/<int:id>/',  BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:id>/',  BookDelete.as_view(), name='book_delete'),

    path('author/list/',               AuthorList.as_view(), name='author_list'),
    path('author/<int:id>/',           AuthorDetail.as_view(), name='author_detail'),
    path('author/add/',                AuthorCreate.as_view(), name='author_create'),
    path('author/update/<int:id>/',    AuthorUpdate.as_view(), name='author_update'),
    path('author/delete/<int:id>/',    AuthorDelete.as_view(), name='author_delete'),


    # path('test/', test),
]
