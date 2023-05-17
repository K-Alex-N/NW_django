from django import forms

PROD_MAX_COUNT = [(i, str(i)) for i in range(1, 26)]

class BasketAddProductForm(forms.Form):
    # coerce ???
    # what for label ???
    # initial ?
    # update ? maybe delete ?
    count_prod = forms.TypedChoiceField(choices=PROD_MAX_COUNT, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)