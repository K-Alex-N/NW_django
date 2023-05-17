from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from basket.basket_logic import Basket
from basket.forms import BasketAddProductForm
from library.models import Book
from library.utils import menu


def basket_list(request):
    return render(request, 'basket.html', {'basket': Basket(request), 'menu': menu})


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Book, pk=product_id)
    form = BasketAddProductForm(request.POST)

    if form.is_valid():
        basket_info = form.cleaned_data
        basket.add(
            product=product_obj,
            count_product=basket_info['count_prod'],
        )

    return redirect('basket_list')


def basket_remove(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Book, pk=product_id)
    basket.remove(product_obj)
    return redirect('basket_list')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('book_list')
