from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from library.models import Book, Author, Publisher
from library.serializers import BookSerializer


class BookAPITest(APITestCase):
    def test_get_list(self):
        a = Author(name='x')
        a.save()

        p = Publisher(name='x', contact_name='x', email='email@email.email', phone_number='x', )
        p.save()

        book1 = Book.objects.create(name='x', author=a, publisher=p, description='x', price=1, )

        response = self.client.get(reverse('api_book_list'))
        serializer_data = {'book_list': BookSerializer([book1], many=True).data}

        self.assertEqual(serializer_data, response.data)


class BookSerializerTestCase(TestCase):
    def test_serializer(self):
        a = Author(name='x')
        a.save()

        p = Publisher(name='x', contact_name='x', email='email@email.email', phone_number='x', )
        p.save()

        book1 = Book.objects.create(name='x', author=a, publisher=p, description='x', price=1, )

        serializer_data = BookSerializer([book1], many=True).data
        expected_data = [
            {
                'name': 'x',
                'author': 1,
                'publisher': 1,
                'description': 'x',
                'image': None,
                'price': 1,
                'is_not_visible': False,
            }
        ]

        self.assertEqual(serializer_data, expected_data)
