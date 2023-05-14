from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from library.forms import *
from library.models import *
from library.utils import *
from study_lib import settings


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

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['message']
            mail = send_mail(
                'Спасибо за обратную связь',
                f'Ваще обращение принято.\n{msg}',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False
            )
            if mail:
                return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'library/feedback.html', {'form': form, 'menu': menu})


# ---------------------------------------------------------------- #
# Auth
# ---------------------------------------------------------------- #

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'library/auth_register.html'
    success_url = reverse_lazy('login')
    title = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'library/auth_login.html'
    title = 'Вход'

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
    title = 'Список книг'


class BookDetail(DataMixin, DetailView):
    model = Book
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def get_title(self):
        return self.object.name


class BookCreate(DataMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = reverse_lazy('book_list')
    title = 'Добавить книгу'
    # success_url = reverse_lazy('book_detail', )  # не работает!!!

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
    title = 'Изменить книгу'
    # success_url = reverse_lazy('book.get_absolute_url()') # нужно проверить!!!


class BookDelete(DataMixin, DeleteView):
    model = Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

# ---------------------------------------------------------------- #
# Author
# ---------------------------------------------------------------- #

class AuthorList(DataMixin, ListView):
    model = Author
    title = 'Список авторов'


class AuthorDetail(DataMixin, DetailView):
    model = Author
    pk_url_kwarg = 'id'

    def get_title(self):
        return self.object.name


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