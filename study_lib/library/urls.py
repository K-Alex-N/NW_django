from django.urls import path

from .views import *

urlpatterns = [

    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),

    path('api/book/', book_api_list, name='api_book_list'),
    path('api/book/<int:pk>/', book_api_detail, name='api_book_detail'),

    path('register/',   RegisterUser.as_view(), name='register'),
    path('login/',      LoginUser.as_view(),    name='login'),
    path('logout/',     logout_user,            name='logout'),

    path('book/list/',             BookList.as_view(),              name='book_list'),
    path('book/list_with_hidden/', BookListWithHidden.as_view(),    name='book_list_with_hidden'),
    path('book/<int:pk>/',         BookDetail.as_view(),            name='book_detail'),
    path('book/add/',              BookCreate.as_view(),            name='book_create'),
    path('book/update/<int:pk>/',  BookUpdate.as_view(),            name='book_update'),
    path('book/delete/<int:pk>/',  BookDelete.as_view(),            name='book_delete'),

    path('author/list/',               AuthorList.as_view(),   name='author_list'),
    path('author/<int:pk>/',           AuthorDetail.as_view(), name='author_detail'),
    path('author/add/',                AuthorCreate.as_view(), name='author_create'),
    path('author/update/<int:pk>/',    AuthorUpdate.as_view(), name='author_update'),
    path('author/delete/<int:pk>/',    AuthorDelete.as_view(), name='author_delete'),

    path('publisher/list/',             PublisherList.as_view(),   name='publisher_list'),
    path('publisher/<int:pk>/',         PublisherDetail.as_view(), name='publisher_detail'),
    path('publisher/add/',              PublisherCreate.as_view(), name='publisher_create'),
    path('publisher/update/<int:pk>/',  PublisherUpdate.as_view(), name='publisher_update'),
    path('publisher/delete/<int:pk>/',  PublisherDelete.as_view(), name='publisher_delete'),

]
