from django import forms

PROD_MAX_COUNT = [(i, str(i)) for i in range(1, 16)]

class BasketAddProductForm(forms.Form):
    count_prod = forms.TypedChoiceField(choices=PROD_MAX_COUNT, coerce=int, label='Количество')