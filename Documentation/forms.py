from django import forms

class ContactUsMessage(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام فرستنده','maxlength':150})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'موضوع','maxlength':70})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ایمیل','maxlength':170})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'متن پیام (500 کاراکتر)','maxlength':500})
    )