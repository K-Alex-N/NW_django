from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from library.models import *

# ---------------------------------------------------------------- #
# Feedback
# ---------------------------------------------------------------- #

FEEDBACK_TYPES = [
    (1, "Предложение"),
    (2, "Сообщение об ошибке"),
    (3, "Вопрос"),
    (4, "Другое"),
]


class FeedbackForm(forms.Form):
    type = forms.ChoiceField(
        label='Тип сообщения',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=FEEDBACK_TYPES)

    message = forms.CharField(
        label='Cообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))


# ---------------------------------------------------------------- #
# Authentication
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
# Book, Author, Publisher
# ---------------------------------------------------------------- #

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        msg = 'Если автора нет, то необходимо его <a href="/author/add/">создать</a>.'
        self.fields['author'].help_text = msg
        msg2 = 'Если издательства нет, то необходимо его <a href="/publisher/add/">создать</a>.'
        self.fields['publisher'].help_text = msg2

    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'description', 'image', 'pages', 'cover', 'dimensions', 'public_date',
                  'price', 'is_not_visible']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название книги'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'publisher': forms.Select(attrs={'class': 'form-select'}),
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
        super(BookForm, self).clean()
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')

        if not description or len(description.split()) < 5:
            self._errors['description'] = self.error_class(['Требуется минимум 5 слов.'])
        if not price or price < 10:
            self._errors['price'] = self.error_class(['Цена должна быть минимум 10.'])
        return self.cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Биография', 'rows': 7})
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description', 'contact_name', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'издательство'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'описание', 'rows': 7}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО агента'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'почта'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'телефон'}),
        }
