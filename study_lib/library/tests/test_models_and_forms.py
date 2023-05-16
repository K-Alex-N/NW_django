"""
The philosophy for testing your forms is the same as for testing your models; you need to test anything
that you've coded or your design specifies, but not the behavior of the underlying framework
and other third party libraries.

Generally this means that you should test that the forms have the fields that you want,
and that these are displayed with appropriate labels and help text. You don't need to verify
that Django validates the field type correctly (unless you created your own custom field and validation)
— i.e. you don't need to test that an email field only accepts emails.
However you would need to test any additional validation that you expect to be performed on the
fields and any messages that your code will generate for errors.
"""

from unittest import TestCase

from library.forms import *
from library.models import *


class ModelsAndFormsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            name='name',
        )

        Publisher.objects.create(
            name='name',
            contact_name='contact_name',
            email='email@email.email',
            phone_number='phone_number',
        )

        Book.objects.create(
            name='name',
            author=1,
            publisher=1,
            description='description',
            price=1,
        )

    def test_Book(self):
        book = Book.objects.get(id=1)

        # name verbose_name
        field_verbose_name = book._meta.get_field('name').verbose_name
        self.assertEqual(field_verbose_name, 'название')

        # name max_length
        max_length = book._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

        # __str__
        expected_object_name = book.name
        self.assertEqual(str(book), expected_object_name)

        # get_absolute_url
        self.assertEqual(book.get_absolute_url(), '/book/1/')

    def test_Author(self):
        author = Author.objects.get(id=1)
        field_verbose_name = author._meta.get_field('name').verbose_name
        self.assertEqual(field_verbose_name, 'автор')

    def test_BookForm(self):
        form = BookForm()

        msg = 'Если автора нет, то необходимо его <a href="/author/add/">создать</a>.'
        self.assertTrue(form.fields['author'].help_text == msg)

        msg2 = 'Если издательства нет, то необходимо его <a href="/publisher/add/">создать</a>.'
        self.assertTrue(form.fields['publisher'].help_text == msg2)

        # description check
        form = BookForm(data={
            'description': 'два слова',
            'price': 10,
            'name': '___',
            'author': 1,
            'publisher': 1,
        })
        self.assertFalse(form.is_valid())

        # price check
        form = BookForm(data={
            'description': 'п я т ь слов',
            'price': -100,
            'name': '___',
            'author': 1,
            'publisher': 1,
        })
        self.assertFalse(form.is_valid())

        form = BookForm(data={
            'description': 'п я т ь слов',
            'price': 10,
            'name': '___',
            'author': 1,
            'publisher': 1,
        })
        self.assertTrue(form.is_valid())
