from django.test import TestCase
from django.urls import reverse

from library.models import Book, Author, Publisher


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        n = 5
        # Create 5 books for pagination tests
        for i in range(n):
            a = Author(name=i)
            a.save()

            p = Publisher(
                name=i,
                contact_name=i,
                email=f'email{i}@email.email',
                phone_number=i,
            )
            p.save()

            Book.objects.create(
                name=i,
                author=a,
                publisher=p,
                description=i,
                price=1,
            )

    def test_book_url_hard(self):
        response = self.client.get('/book/list/')
        self.assertEqual(response.status_code, 200)

    def test_book_url_by_name(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, 'library/book_list.html')

    def test_book_pagination_is_3(self):
        response = self.client.get(reverse('book_list'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['book_list']), 3)

    def test_book_page2(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        response = self.client.get(reverse('book_list') + '?page=2')
        self.assertEqual(len(response.context['book_list']), 2)
