from django import forms

from library.models import Author, Book


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        msg = r'Если автора нет в списке, то вначале необходимо его <a href="/all_books/">создать</a>.'
        self.fields['author'].help_text = msg

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название книги'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество страниц'}),
            'cover': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Обложка'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Размеры'}),
            'public_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата публикации'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'is_not_visible': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'})}

    def clean(self):

        super(AddBookForm, self).clean()
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')

        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        return self.cleaned_data

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 3:
    #         raise forms.ValidationError('Длина меньше 3х символов')
    #
    #     return name


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


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
