class Menu():
    bottom_center = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Книги', 'url': '/book/list/'},
    ]
    right = [
        {'title': 'Список книг', 'url': 'all_books'},
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

    def get_menu(self, **context):
        context['menu'] = menu
        return context