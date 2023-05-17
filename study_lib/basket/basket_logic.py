from copy import deepcopy

from library.models import Book
from study_lib import settings


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
            # session delete from here
        self.basket = basket

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True # delete


    def add(self, product, count_product=1, update_count=False):
        # update_count delete and refactor all method
        prod_pk = str(product.pk)

        if prod_pk not in self.basket:
            self.basket[prod_pk] = {
                'count_prod': 0,
                'price_prod': str(product.price)
            }

        if update_count:
            self.basket[prod_pk]['count_prod'] = count_product
        else:
            self.basket[prod_pk]['count_prod'] += count_product

        self.save()

    def remove(self, product):
        prod_pk = str(product.pk)

        if prod_pk in self.basket:
            del self.basket[prod_pk]
            self.save()

    def get_total_price(self):
        return sum(float(item['price_prod']) * int(item['count_prod']) for item in self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True
        # what for modified True

    def __len__(self):
        return sum(int(item['count_prod']) for item in self.basket.values())

    def __iter__(self):
        list_prod_pk = self.basket.keys()

        list_prod_obj = Book.objects.filter(pk__in=list_prod_pk)

        # basket = self.basket.copy()
        basket = deepcopy(self.basket)

        for prod_obj in list_prod_obj:
            basket[str(prod_obj.pk)]['book'] = prod_obj

        for item in basket.values():
        # for item in basket.keys():
            item['total_price'] = float(item['price_prod']) * int(item['count_prod'])
            yield item
