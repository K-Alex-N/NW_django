# Generated by Django 4.2.1 on 2023-05-08 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book', to='library.author', verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_not_visible',
            field=models.BooleanField(default=False, verbose_name='скрыто?'),
        ),
    ]
