from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
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


# def home(request):
#     menu_copy = deepcopy(menu)
#     menu_copy['bottom_center'].pop()
#     return render(request, 'library/index.html', {'title': 'Домашняя страница', 'menu': menu_copy})


def page_not_found(request, exception):
    return HttpResponseNotFound('not found')


# ---------------------------------------------------------------- #
# Feedback
# ---------------------------------------------------------------- #

@login_required
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
    template_name = 'library/auth/register.html'
    title = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book_list')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'library/auth/login.html'
    title = 'Вход'

    def get_success_url(self):
        return reverse_lazy('book_list')


def logout_user(request):
    logout(request)
    return redirect('login')


# ---------------------------------------------------------------- #
# Book
# ---------------------------------------------------------------- #


class PermissionBookMixin(PermissionRequiredMixin):
    permission_required = [
        "library.add_book",
        "library.change_book",
        "library.delete_book",
    ]


class BookMixin:
    model = Book
    paginate_by = 3


class BookList(DataMixin, BookMixin, ListView):
    title = 'Список книг'
    queryset = Book.objects.filter(is_not_visible=False)


class BookListWithHidden(DataMixin, BookMixin, ListView):
    title = 'Список книг'


class BookDetail(DataMixin, BookMixin, DetailView):
    def get_title(self):
        return self.object.name


class BookCreate(DataMixin, BookMixin, PermissionBookMixin, CreateView):
    form_class = BookForm
    title = 'Добавить книгу'


class BookUpdate(DataMixin, BookMixin, PermissionBookMixin, UpdateView):
    form_class = BookForm
    title = 'Изменить книгу'


class BookDelete(DataMixin, BookMixin, PermissionBookMixin, DeleteView):
    success_url = reverse_lazy('book_list')


# ---------------------------------------------------------------- #
# Author
# ---------------------------------------------------------------- #

class PermissionAuthorMixin(PermissionRequiredMixin):
    permission_required = [
        "library.view_author",
        "library.add_author",
        "library.change_author",
        "library.delete_author",
    ]


class AuthorMixin:
    model = Author
    paginate_by = 10


class AuthorList(AuthorMixin, DataMixin, ListView):
    title = 'Список авторов'


class AuthorDetail(AuthorMixin, DataMixin, DetailView):
    def get_title(self):
        return self.object.name


class AuthorCreate(AuthorMixin, DataMixin, PermissionAuthorMixin, CreateView):
    form_class = AuthorForm
    title = 'Добавить автора'


class AuthorUpdate(AuthorMixin, DataMixin, PermissionAuthorMixin, UpdateView):
    form_class = AuthorForm
    title = 'Изменить автора'


class AuthorDelete(AuthorMixin, DataMixin, PermissionAuthorMixin, DeleteView):
    success_url = reverse_lazy('author_list')


# ---------------------------------------------------------------- #
# Publisher
# ---------------------------------------------------------------- #

class PermissionPublisherMixin(PermissionRequiredMixin):
    permission_required = [
        "library.view_publisher",
        "library.add_publisher",
        "library.change_publisher",
        "library.delete_publisher",
    ]


class PublisherMixin:
    model = Publisher
    paginate_by = 10


class PublisherList(PublisherMixin, DataMixin, PermissionPublisherMixin, ListView):
    title = 'Список издательств'


class PublisherDetail(PublisherMixin, DataMixin, PermissionPublisherMixin, DetailView):
    def get_title(self):
        return self.object.name


class PublisherCreate(PublisherMixin, DataMixin, PermissionPublisherMixin, CreateView):
    form_class = PublisherForm
    title = 'Добавить издательство'


class PublisherUpdate(PublisherMixin, DataMixin, PermissionPublisherMixin, UpdateView):
    form_class = PublisherForm
    title = 'Изменить издательство'


class PublisherDelete(PublisherMixin, DataMixin, PermissionPublisherMixin, DeleteView):
    success_url = reverse_lazy('publisher_list')
