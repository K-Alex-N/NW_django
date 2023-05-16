# from unittest import TestCase
#
# from library.models import *
# from library.views import plus
#
#
# class Plus(TestCase):
#     def test_plus(self):
#         res = plus(3, 5)
#         self.assertEqual(res, 8)
#
#
# # class BookModelTest(TestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         Author.objects.create(
# #             name='name',
# #             biography='biography',
# #         )
# #
# #         Publisher.objects.create(
# #             name='name',
# #             description='description',
# #             contact_name='contact_name',
# #             email='email@email.email',
# #             phone_number='phone_number',
# #         )
# #
# #         Book.objects.create(
# #             name='name',
# #             author='1',
# #             publisher='1',
# #             description='description',
# #             price=123,
# #             # is_not_visible =
# #             # blank=True
# #             # image =
# #             # pages = models.IntegerField(blank=True, null=True, verbose_name='количество страниц')
# #             # cover = models.CharField(max_length=200, blank=True, verbose_name='обложка')
# #             # dimensions = models.CharField(max_length=200, blank=True, verbose_name='размеры')
# #             # public_date = models.DateField(blank=True, null=True, verbose_name='дата публикации')
# #             # autofill
# #             # date_create = models.DateField(auto_now_add=True, verbose_name='дата создания карточки товара')
# #             # date_update = models.DateField(auto_now=True, verbose_name='дата изменения карточки товара')
# #         )
# #
# #     def test_author(self):
# #         author = Author.objects.get(id=1)
# #         field_label = author._meta.get_field('name').verbose_name
# #         self.assertEqual(field_label, 'name')
#
#
