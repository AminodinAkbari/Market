from django.contrib import admin
from django.urls import path,re_path,include
from Market_Product.views import *

from django.conf import settings
from django.conf.urls.static import static

from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name='Home'),
    path('navbar',include('Market_Navbar.urls')),
    path('header_off_banner',include('Market_OFFs_Banners.urls')),
    path('',include('Market_Product.urls'), name='product_detail'),
    path('',include('Market_Accounts.urls')),
    path('',include('Market_Cart.urls')),
    path('Docs/',include('Documentation.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)