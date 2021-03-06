from django import forms 
from django.forms import NumberInput
from django.core import validators
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]




class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField( min_value=1, widget=NumberInput(attrs={'class': 'form-control text-center','value': 1, 'max':3 }))
    # override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    taille   = forms.CharField(max_length=20, required=True)
    color    = forms.CharField(max_length=20, required=True)

