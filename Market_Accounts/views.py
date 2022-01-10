from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from Market_Accounts.models import Profile
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def Login_veiw(request):

    if request.user.is_authenticated:
        return redirect('/')

    Form = LoginForm(request.POST or None)
    if Form.is_valid():
        user_name = Form.cleaned_data.get('username')
        password = Form.cleaned_data.get('password')
        user = authenticate(request,username = user_name,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            Form.add_error('username','نام کاربری یا رمز عبور اشتباه است')
    return render(request,'accounts/login.html',{'form':Form})

@login_required(login_url='/login')
def Logout_view(request):
    logout(request)
    return redirect('/')

def Register_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    Form = RegisterForm(request.POST or None)
    if Form.is_valid():
        user_name = Form.cleaned_data.get('username')
        email = Form.cleaned_data.get('email')
        password = Form.cleaned_data.get('password')
        first_name = Form.cleaned_data.get('firstname')
        last_name = Form.cleaned_data.get('lastname')
        gender = Form.cleaned_data.get('gender')
        # profile_pic = Form.cleaned_data.get('profile_pic')
        # print(profile_pic)
        User.objects.create_user(username=user_name,password=password,email=email,first_name=first_name,last_name=last_name)
        # return redirect('/login')
        user = authenticate(request,username=user_name,password=password)
        Profile.objects.create(user =user ,gender = gender)
        if user is not None:
            login(request,user)
            return redirect('/')
    context = {
        'register_form':Form
    }
    return render(request,'accounts/register.html',context)