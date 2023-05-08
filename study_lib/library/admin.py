from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'is_not_visible', 'date_update', 'date_create']
    list_filter = ['is_not_visible', 'author', 'date_create', 'date_update']
    search_fields = ['name', 'author__name']
    list_editable = ['price', 'is_not_visible', ]


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookOrder)
admin.site.register(Order)
