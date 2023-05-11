from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from library.forms import AddBookForm
from library.models import Book
from library.utils import DataMixin


def home(request):
    context = {
        'title': 'Домашняя страница',
    }
    return render(request, 'library/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('not found')

class BooksView(DataMixin, ListView):
    model = Book
    # queryset = Book.objects.filter(is_not_visible=False)
    template_name = 'library/all_books.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Список книг'))
        return context


class AddBook(DataMixin, CreateView):
    form_class = AddBookForm
    template_name = 'library/add_book.html'
    success_url = reverse_lazy('all_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Добавить книгу'))
        return context


class BookDetail(DataMixin, DetailView):
    model = Book
    template_name = 'library/book_description.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title=context['book']))
        return context

