from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    cover = models.CharField(max_length=200, blank=True)
    dimensions = models.CharField(max_length=200, blank=True)
    public_date = models.DateField(blank=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    is_visible = models.BooleanField(default=True)

