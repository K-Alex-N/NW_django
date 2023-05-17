from copy import deepcopy

menu = {
    'bottom_center': [
        # {'title': 'Home',           'url': 'home'},
        {'title': 'Книги',          'url': 'book_list'},
        {'title': 'Обратная связь', 'url': 'feedback',      'for_authorized': True},
        {'title': 'Корзина',        'url': 'basket_list',   'for_authorized': True},
    ],
    'right': [
        {'title': 'Список книг',            'url': 'book_list_with_hidden'},
        {'title': 'Добавить книгу',         'url': 'book_create'},
        {'title': 'Список авторов',         'url': 'author_list'},
        {'title': 'Добавить автора',        'url': 'author_create'},
        {'title': 'Список издательств',     'url': 'publisher_list'},
        {'title': 'Добавить издательство',  'url': 'publisher_create'},
    ]
}


class DataMixin:
    title = None
    basket_form = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()

        menu_copy = deepcopy(menu)
        if not self.request.user.is_authenticated:
            menu_copy['bottom_center'].pop()
        context['menu'] = menu_copy

        if self.basket_form:
            context['basket_form'] = self.basket_form

        return context

