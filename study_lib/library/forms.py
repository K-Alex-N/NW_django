from django import forms

from library.models import Author


class BookForm(forms.Form):
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all())
    name = forms.CharField(label='Название книги', min_length=5, strip=True)
    description = forms.CharField(label='Описание', widget=forms.Textarea, strip=True)
    image = forms.ImageField(label='Изображение', required=False)
    pages = forms.IntegerField(label='Количество страниц', required=False)
    price = forms.IntegerField(label='Цена', min_value=10)
    cover = forms.CharField(label='Обложка', strip=True)
    dimensions = forms.CharField(label='Размеры', strip=True)
    public_date = forms.DateField(label='Дата публикации')
