from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from library.models import Author, Book


# ---------------------------------------------------------------- #
# Auth
# ---------------------------------------------------------------- #

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Логин'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Логин'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password']


# ---------------------------------------------------------------- #
# Book
# ---------------------------------------------------------------- #
class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        msg = 'Если автора нет в списке, то вначале необходимо его <a href="/add_author/">создать</a>.'
        self.fields['author'].help_text = msg

    class Meta:
        model = Book
        fields = ['name', 'author', 'description', 'image', 'pages', 'cover', 'dimensions', 'public_date', 'price',
                  'is_not_visible']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название книги'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество страниц'}),
            'cover': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Обложка'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Размеры'}),
            'public_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата публикации'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'is_not_visible': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'})}

    def clean(self):
        super(AddBookForm, self).clean()
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')

        # добавить проверку на уникальность названия книги
        # https://www.agiliq.com/blog/2019/01/django-createview/
        # def clean_title(self):
        #     title = self.cleaned_data['title']
        #     if Book.objects.filter(user=self.user, title=title).exists():
        #         raise forms.ValidationError("You have already written a book with same title.")
        #     return title
        if not description or len(description.split()) < 5:
            self._errors['description'] = self.error_class(['Требуется минимум 5 слов.'])
        if not price or price < 10:
            self._errors['price'] = self.error_class(['Цена должна быть минимум 10.'])
        return self.cleaned_data


# class AddBookForm(forms.Form):
#     name = forms.CharField(
#         label='Название книги', min_length=5, strip=True,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Название книги'}))
#
#     author = forms.ModelChoiceField(
#         label='Автор', queryset=Author.objects.all(), empty_label='---Выберите автора---',
#         widget=forms.Select(attrs={
#             'class': 'form-select', }))
#
#     description = forms.CharField(
#         label='Описание', strip=True,
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'Описание',
#             'rows': 3}))
#
#     image = forms.ImageField(
#         label='Изображение', required=False,
#         widget=forms.ClearableFileInput(attrs={
#             'class': 'form-control',
#             'type': 'file'}))
#
#     pages = forms.IntegerField(
#         label='Количество страниц', required=False,
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Количество страниц'}))
#
#     cover = forms.CharField(
#         label='Обложка', strip=True, required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Обложка'}))
#
#     dimensions = forms.CharField(
#         label='Размеры', strip=True, required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Размеры'}))
#
#     public_date = forms.DateField(
#         label='Дата публикации', required=False,
#         widget=forms.DateInput(attrs={
#             'class': 'form-control',
#             'type': 'date',
#             'placeholder': 'Дата публикации'}))
#
#     price = forms.IntegerField(
#         label='Цена', min_value=10,
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Цена'}))
#
#     is_not_visible = forms.BooleanField(
#         label='Скрыть',
#         widget=forms.CheckboxInput(attrs={
#             'class': 'form-check-input',
#             'type': 'checkbox'}))

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
