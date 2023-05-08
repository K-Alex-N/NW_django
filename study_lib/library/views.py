from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from library.forms import BookForm
from library.models import Book


def home(request):
    context = {
        'title': 'Домашняя страница',
    }
    return render(request, 'library/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('not found')


def all_books(request):
    books = Book.objects.filter(is_not_visible=False)
    context = {
        'title': 'All books',
        'books': books
    }
    return render(request, 'library/all_books.html', context=context)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
        return redirect('all_books')

    form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})


def book_description(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'library/book_description.html', context=context)

# raise Http404() - если нужно перенаправиль на 404
