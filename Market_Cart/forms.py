from django import forms

class NewOrderForm(forms.Form):
    # product_id = forms.CharField(
    #     widget=forms.HiddenInput()
    # )
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'value':1})
    )