from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from basket.forms import BasketAddProductForm
from library.forms import *
from library.models import *
from library.serializers import BookSerializer
from library.utils import *
from study_lib import settings


def page_not_found(request, exception):
    return HttpResponseNotFound('not found')


def home(request):
    context = {
        'title': 'Домашняя страница',
        'menu': menu,
    }
    return render(request, 'library/index.html', context=context)


# ---------------------------------------------------------------- #
# API
# ---------------------------------------------------------------- #

@api_view(['GET', 'POST'])
def book_api_list(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        serializer = BookSerializer(book_list, many=True)
        return Response({'book_list': serializer.data})
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_api_detail(request, pk, format=None):
    book_obj = get_object_or_404(Book, pk=pk)
    if not book_obj.is_not_visible:
        if request.method == 'GET':
            serializer = BookSerializer(book_obj)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BookSerializer(book_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data added successfully', 'book': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            book_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


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


class BookMixin(DataMixin):
    model = Book
    paginate_by = 3


class BookList(BookMixin, ListView):
    title = 'Список книг'
    queryset = Book.objects.filter(is_not_visible=False)
    basket_form = BasketAddProductForm()


class BookListWithHidden(BookMixin, ListView):
    title = 'Список книг'


class BookDetail(BookMixin, DetailView):
    basket_form = BasketAddProductForm()

    def get_title(self):
        return self.object.name


class BookCreate(BookMixin, PermissionBookMixin, CreateView):
    form_class = BookForm
    title = 'Добавить книгу'


class BookUpdate(BookMixin, PermissionBookMixin, UpdateView):
    form_class = BookForm
    title = 'Изменить книгу'


class BookDelete(BookMixin, PermissionBookMixin, DeleteView):
    success_url = reverse_lazy('book_list')


# ---------------------------------------------------------------- #
# Author
# ---------------------------------------------------------------- #


class AuthorMixin(DataMixin, PermissionRequiredMixin):
    model = Author
    paginate_by = 10

    permission_required = [
        "library.view_author",
        "library.add_author",
        "library.change_author",
        "library.delete_author",
    ]


class AuthorList(AuthorMixin, ListView):
    title = 'Список авторов'


class AuthorDetail(AuthorMixin, DetailView):
    def get_title(self):
        return self.object.name


class AuthorCreate(AuthorMixin, CreateView):
    form_class = AuthorForm
    title = 'Добавить автора'


class AuthorUpdate(AuthorMixin, UpdateView):
    form_class = AuthorForm
    title = 'Изменить автора'


class AuthorDelete(AuthorMixin, DeleteView):
    success_url = reverse_lazy('author_list')


# ---------------------------------------------------------------- #
# Publisher
# ---------------------------------------------------------------- #

class PublisherMixin(DataMixin, PermissionRequiredMixin):
    model = Publisher
    paginate_by = 10

    permission_required = [
        "library.view_publisher",
        "library.add_publisher",
        "library.change_publisher",
        "library.delete_publisher",
    ]


class PublisherList(PublisherMixin, ListView):
    title = 'Список издательств'


class PublisherDetail(PublisherMixin, DetailView):
    def get_title(self):
        return self.object.name


class PublisherCreate(PublisherMixin, CreateView):
    form_class = PublisherForm
    title = 'Добавить издательство'


class PublisherUpdate(PublisherMixin, UpdateView):
    form_class = PublisherForm
    title = 'Изменить издательство'


class PublisherDelete(PublisherMixin, DeleteView):
    success_url = reverse_lazy('publisher_list')
