from django import forms
from .models import Product, Review

rates = [
    ('None' , '(امتیاز شما برای این محصول)'),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]

class ReviewForm(forms.Form):
    rate = forms.ChoiceField(widget=forms.Select, choices=rates)   
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','id':'comment-input','placeholder':'نظر خود را بنویسید (پس از تایید ، در همین صفحه نمایش داده خواهد شد)'}),
        label='متن دیدگاه'
    )  