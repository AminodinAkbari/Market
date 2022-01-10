from django import forms
from .models import Review

rates = [
    ('None' , '(امتیاز شما برای این محصول)'),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]

class ReviewForm(forms.Form):
    rate = forms.CharField(
            widget=forms.TextInput,
            label='به این محصول چه امتیازی می دهید ؟',
        )   
    # rate = forms.CharField(
    #     widget=forms.TextInput(attrs={'class':'form-control','id':'comment-input','placeholder':'نظر خود را بنویسید (پس از تایید ، در همین صفحه نمایش داده خواهد شد)'}),
    #     label=''
    # )  
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','id':'comment-input','placeholder':'نظر خود را بنویسید (پس از تایید ، در همین صفحه نمایش داده خواهد شد)'}),
        label=''
    )  