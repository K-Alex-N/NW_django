class Menu():
    bottom_center = [
        {'title': 'Home',           'url': 'home'},
        {'title': 'Книги',          'url': 'book_list'},
        {'title': 'Обратная связь', 'url': 'feedback'},
    ]
    right = [
        {'title': 'Список книг',            'url': 'book_list'},
        {'title': 'Добавить книгу',         'url': 'book_create'},
        {'title': 'Список авторов',         'url': 'author_list'},
        {'title': 'Добавить автора',        'url': 'author_create'},
        {'title': 'Список издательств',     'url': 'publisher_list'},
        {'title': 'Добавить издательство',  'url': 'publisher_create'},
    ]


menu = Menu()


class DataMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = self.get_title()
        return context

