from django.conf.urls.static import static
from django.urls import path

from study_lib import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('all_books/', all_books, name='all_books'),
    path('book/<int:book_id>/', book_description, name='book_description'),
]

if settings.DEBUG: # чтобы в режиме отладки добавить вот эти маршруты
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
