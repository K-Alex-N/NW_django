class Menu():
    bottom_center = [
        {'title': 'Home', 'url': '/'},
        {'title': 'All books', 'url': '/all_books'},
        {'title': 'Add book', 'url': '/add'}
    ]


menu = Menu()


class DataMixin:
    paginate_by = 3

    def get_menu(self, **context):
        context['menu'] = menu
        return context