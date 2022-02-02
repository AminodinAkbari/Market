from django import forms
from django.contrib.auth.models import User
from captcha import fields,widgets
from captcha.widgets import ReCaptchaV2Invisible

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','id':'username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}),
    )
    captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox()
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری','class':'form-control'}),
    )
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام','class':'form-control'}),
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی','class':'form-control'}),
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'تلفن','class':'form-control','maxlength':'11'}),
    )

    Gender = (
        ('woman', 'زن'),
        ('man', 'مرد'),
    )
    gender = forms.ChoiceField(
        choices = Gender,
        widget=forms.Select(attrs={'class':'form-control'})
        )

    img = forms.FileField()

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور','class':'form-control mb-3'}),
        label='رمز عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور (تکرار)','class':'form-control mb-3'}),
        label='رمز عبور (تکرار)'
    )

    captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox()
    )

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if len(password)<8:
            raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')

        if password != re_password :
            raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist = User.objects.filter(email=email).exists()

        if is_exist:
            raise forms.ValidationError('ایمیل قبلا در سایت ثبت شده است')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist = User.objects.filter(username=username).exists()

        if is_exist:
            raise forms.ValidationError('نام کاربری قبلا در سایت ثبت شده است')
        return username

    def profile_pic_url (self):
        if self.profile_pic: return self.image.url
        else: return None