from django.urls import path
from .views import main_off_banner
urlpatterns = [
    path('', main_off_banner),
]