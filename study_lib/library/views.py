from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from library.forms import AddBookForm
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
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddBookForm()

    return render(request, 'library/add_book.html', {'form': form})


def book_description(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_description.html', {'book': book})


def test(request):
    return render(request, 'library/test.html')

# raise Http404() - если нужно перенаправиль на 404
