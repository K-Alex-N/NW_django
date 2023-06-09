# Generated by Django 4.2.1 on 2023-05-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_book_public_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookorder',
            options={'verbose_name': 'позиция заказа', 'verbose_name_plural': 'позиции заказов'},
        ),
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, verbose_name='биография'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_not_visible',
            field=models.BooleanField(default=False, verbose_name='скрыть'),
        ),
    ]
