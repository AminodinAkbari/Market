from django.urls import path,re_path,include
from .views import Login_veiw,Logout_view,Register_view,google,user_panel

urlpatterns = [
    path('login',Login_veiw),
    path('logout',Logout_view),
    path('register',Register_view),
    path('google',google),
    path('user_panel',user_panel),
]