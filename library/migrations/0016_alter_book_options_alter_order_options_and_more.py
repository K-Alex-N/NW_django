# Generated by Django 4.2.1 on 2023-05-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_bookorder_price_bookorder_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['date_create'], 'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['order_date'], 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='название'),
        ),
    ]
