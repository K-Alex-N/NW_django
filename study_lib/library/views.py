from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from library.forms import *
from library.models import *
from library.utils import *


def home(request):
    context = {
        'title': 'Домашняя страница',
        'menu': menu,
    }
    return render(request, 'library/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('not found')

# ---------------------------------------------------------------- #
# Feedback
# ---------------------------------------------------------------- #

def feedback():


# ---------------------------------------------------------------- #
# Auth
# ---------------------------------------------------------------- #

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'library/auth_register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Регистрация'))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'library/auth_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Вход'))
        return context

    def get_success_url(self):
        return reverse_lazy('book_list')


def logout_user(request):
    logout(request)
    return redirect('login')


# ---------------------------------------------------------------- #
# Book
# ---------------------------------------------------------------- #

class BookList(DataMixin, ListView):
    model = Book
    queryset = Book.objects.filter(is_not_visible=False)
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Список книг'))
        return context


class BookDetail(DataMixin, DetailView):
    model = Book
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title=context['book']))
        return context


class BookCreate(DataMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = reverse_lazy('book_list')

    # success_url = reverse_lazy('book_detail', )  # не работает!!!

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Добавить книгу'))
        return context


# class BookCreateView(CreateView):
#     def get(self, request, *args, **kwargs):
#         context = {'form': BookCreateForm()}
#         return render(request, 'books/book-create.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = BookCreateForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             book.save()
#             return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
#         return render(request, 'books/book-create.html', {'form': form})


class BookUpdate(DataMixin, UpdateView):
    model = Book
    form_class = AddBookForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

    # success_url = reverse_lazy('book.get_absolute_url()') # нужно проверить!!!

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Изменить книгу'))
        return context


class BookDelete(DataMixin, DeleteView):
    model = Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

# ---------------------------------------------------------------- #
# Author
# ---------------------------------------------------------------- #

class AuthorList(DataMixin, ListView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('\n' * 5)
        print('!!!!!!!', context)
        context.update(self.get_menu(title='Список авторов'))
        return context


class AuthorDetail(DataMixin, DetailView):
    model = Author
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title=context['object']))
        return context


class AuthorCreate(DataMixin, CreateView):
    model = Author
    # form_class = AddBookForm
    # success_url = reverse_lazy('book_list')

    # success_url = reverse_lazy('book_detail', )  # не работает!!!

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Добавить книгу'))
        return context


# class BookCreateView(CreateView):
#     def get(self, request, *args, **kwargs):
#         context = {'form': BookCreateForm()}
#         return render(request, 'books/book-create.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = BookCreateForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             book.save()
#             return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
#         return render(request, 'books/book-create.html', {'form': form})


class AuthorUpdate(DataMixin, UpdateView):
    model = Author
    # form_class = AddBookForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

    # success_url = reverse_lazy('book.get_absolute_url()') # нужно проверить!!!

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_menu(title='Изменить книгу'))
        return context


class AuthorDelete(DataMixin, DeleteView):
    model = Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')