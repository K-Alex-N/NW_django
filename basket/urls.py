from django.urls import path

from .views import *

urlpatterns = [
    path('',                    basket_list, name='basket_list'),
    path('add/<int:product_id>/',   basket_add,     name='basket_add'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('clear/',                  basket_clear,   name='basket_clear'),
]