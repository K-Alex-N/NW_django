from django import forms

from library.models import Author


class BookForm(forms.Form):
    name = forms.CharField(
        label='Название книги', min_length=5, strip=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название книги'}))

    author = forms.ModelChoiceField(
        label='Автор', queryset=Author.objects.all(), empty_label='---Выберите автора---',
        widget=forms.Select(attrs={
            'class': 'form-select', }))

    description = forms.CharField(
        label='Описание', strip=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Описание',
            'rows': 3}))

    image = forms.ImageField(
        label='Изображение', required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'type': 'file'}))

    pages = forms.IntegerField(
        label='Количество страниц', required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Количество страниц'}))

    cover = forms.CharField(
        label='Обложка', strip=True, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Обложка'}))

    dimensions = forms.CharField(
        label='Размеры', strip=True, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Размеры'}))

    public_date = forms.DateField(
        label='Дата публикации', required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Дата публикации'}))

    price = forms.IntegerField(
        label='Цена', min_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Цена'}))

    is_not_visible = forms.BooleanField(
        label='Скрыть',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'type': 'checkbox'}))
