from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'is_not_visible', 'date_update', 'date_create']
    list_filter = ['is_not_visible', 'author', 'date_create', 'date_update']
    search_fields = ['name', 'author__name']
    list_editable = ['price', 'is_not_visible', ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography']
    list_filter = ['name']
    search_fields = ['name', 'biography']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'address', 'delivery_price']
    list_filter = ['order_date']
    search_fields = ['address']
    list_editable = ['delivery_price']


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['book', 'order', 'quantity', 'price']
    list_filter = ['book', 'order', 'price']
    search_fields = ['book']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(BookOrder, BookOrderAdmin)
