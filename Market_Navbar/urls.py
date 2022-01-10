from django.urls import path,include
from .views import navbar
urlpatterns = [
    path('',navbar),
    
    ]