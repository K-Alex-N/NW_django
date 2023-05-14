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

class BookMixin:
    model = Book
    form_class = BookForm
    paginate_by = 3


class BookList(DataMixin, BookMixin, ListView):
    title = 'Список книг'
    queryset = Book.objects.filter(is_not_visible=False)


class BookDetail(DataMixin, BookMixin, DetailView):
    def get_title(self):
        return self.object.name


class BookCreate(DataMixin, BookMixin, CreateView):
    title = 'Добавить книгу'

    def get_success_url(self):
        return self.object.get_absolute_url()


class BookUpdate(DataMixin, BookMixin, UpdateView):
    title = 'Изменить книгу'

    def get_success_url(self):
        return self.object.get_absolute_url()


class BookDelete(DataMixin, BookMixin, DeleteView):
    success_url = reverse_lazy('book_list')


# ---------------------------------------------------------------- #
# Author
# ---------------------------------------------------------------- #

class AuthorMixin:
    model = Author
    form_class = AuthorForm
    paginate_by = 5


class AuthorList(AuthorMixin, DataMixin, ListView):
    title = 'Список авторов'


class AuthorDetail(AuthorMixin, DataMixin, DetailView):
    def get_title(self):
        return self.object.name


class AuthorCreate(AuthorMixin, DataMixin, CreateView):
    title = 'Добавить автора'

    def get_success_url(self):
        return self.object.get_absolute_url()


class AuthorUpdate(AuthorMixin, DataMixin, UpdateView):
    title = 'Изменить автора'

    def get_success_url(self):
        return self.object.get_absolute_url()


class AuthorDelete(AuthorMixin, DataMixin, DeleteView):
    success_url = reverse_lazy('author_list')


# ---------------------------------------------------------------- #
# Publisher
# ---------------------------------------------------------------- #

class PublisherMixin:
    model = Publisher
    form_class = PublisherForm
    paginate_by = 5


class PublisherList(PublisherMixin, DataMixin, ListView):
    title = 'Список издательств'


class PublisherDetail(PublisherMixin, DataMixin, DetailView):
    def get_title(self):
        return self.object.name


class PublisherCreate(PublisherMixin, DataMixin, CreateView):
    title = 'Добавить издательство'

    def get_success_url(self):
        return self.object.get_absolute_url()


class PublisherUpdate(PublisherMixin, DataMixin, UpdateView):
    title = 'Изменить издательство'

    def get_success_url(self):
        return self.object.get_absolute_url()


class PublisherDelete(PublisherMixin, DataMixin, DeleteView):
    success_url = reverse_lazy('publisher_list')
