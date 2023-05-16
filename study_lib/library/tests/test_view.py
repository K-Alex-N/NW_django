from django.test import TestCase
from django.urls import reverse

from library.models import Book
# from library.views import


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Create 4 books for pagination tests
        for i in range(11):
            Book.objects.create(
                name=i,
                author=1,
                publisher=1,
                description='description',
                price=1,
            )

    def test_url_by_hard(self):
        response = self.client.get('/book/list/')
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)