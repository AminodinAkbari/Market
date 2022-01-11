from django.urls import path,re_path,include
from .views import add_to_order_detail,Cart,remove_item_fromcart,add_to_favorite
urlpatterns = [
    path('order_detail/<slug>',add_to_order_detail),
    path('favorite/<slug>',add_to_favorite),
    path('cart',Cart),
    path('remove_item_fromcart/<order_id>',remove_item_fromcart),
]