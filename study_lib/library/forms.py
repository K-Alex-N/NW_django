from django import forms

class BookForm(forms.Form):
    name = forms.CharField(label='Название книги', min_length=5, strip=True)
    author = forms.CharField(label='Автор', min_length=5, strip=True)
    description = forms.CharField(label='Описание', widget=forms.Textarea, strip=True)
    image = forms.ImageField(label='Изображение')
    pages = forms.IntegerField(label='количество страниц')
    price = forms.IntegerField(label='цена', min_value=10)
    cover = forms.CharField(label='обложка', strip=True)
    dimensions = forms.CharField(label='размеры', strip=True)
    public_date = forms.DateField(label='дата публикации')
