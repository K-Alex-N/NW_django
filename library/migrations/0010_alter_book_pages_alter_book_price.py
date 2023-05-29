# Generated by Django 4.2.1 on 2023-05-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_image_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, default=1, verbose_name='количество страниц'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=123, verbose_name='цена'),
            preserve_default=False,
        ),
    ]
