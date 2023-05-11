from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='автор', related_name='books')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    is_not_visible = models.BooleanField(default=False, verbose_name='скрыть')
    # blank=True
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='изображение')
    pages = models.IntegerField(blank=True, null=True, verbose_name='количество страниц')
    cover = models.CharField(max_length=200, blank=True, verbose_name='обложка')
    dimensions = models.CharField(max_length=200, blank=True, verbose_name='размеры')
    public_date = models.DateField(blank=True, null=True, verbose_name='дата публикации')
    # autofill
    date_create = models.DateField(auto_now_add=True, verbose_name='дата создания карточки товара')
    date_update = models.DateField(auto_now=True, verbose_name='дата изменения карточки товара')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='автор')
    biography = models.TextField(blank=True, verbose_name='биография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200)
    delivery_price = models.IntegerField()

    books = models.ManyToManyField(Book, through='BookOrder')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'позиция заказа'
        verbose_name_plural = 'позиции заказов'
