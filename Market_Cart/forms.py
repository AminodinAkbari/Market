from django import forms
from Market_Product.models import Product

# qs = Product.objects.get(slug=slug)

class NewOrderForm(forms.Form):
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'value':1})
    )