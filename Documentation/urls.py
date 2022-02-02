from django.urls import path,re_path,include
from .views import DocsList,link,contact_us
urlpatterns = [
    path('', DocsList.as_view()),
    path('contact_us', contact_us),
]