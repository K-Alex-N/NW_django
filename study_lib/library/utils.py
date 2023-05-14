class Menu():
    bottom_center = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Книги', 'url': '/book/list/'},
        {'title': 'Обратная связь', 'url': '/feedback/'},
    ]
    right = [
        {'title': 'Список книг', 'url': 'book_list'},
        {'title': 'Добавить книгу', 'url': 'book_create'},
        {'title': 'Список авторов', 'url': 'author_list'},
        # {'title': 'Добавить автора', 'url': 'author_list'},
        # {'title': 'Список издательств', 'url': 'author_list'},
        # {'title': 'Добавить издательство', 'url': 'author_list'},
        # {'title': 'Добавить книгу', 'url': ''},
        # {'title': 'Добавить книгу', 'url': ''},
        # {'title': 'Добавить книгу', 'url': ''},
        # {'title': 'Добавить книгу', 'url': ''},

    ]


menu = Menu()


class DataMixin:
    paginate_by = 3

    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = self.get_title()
        return context

