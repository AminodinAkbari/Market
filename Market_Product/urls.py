from django.urls import path
from Market_Product.views import product_detail,AllProducts,AllProductsByCategory,ProductSearch,userfavorite,company_page
from Market.views import SideItems

# app_name = 'sub'
urlpatterns = [
    path('product_detail/<slug>',product_detail),
    path('AllProducts',AllProducts.as_view()),
    path('categories/<category_name>',AllProductsByCategory.as_view()),
    path('search',ProductSearch.as_view()),
    path('AllProducts',SideItems),
    path('favorites',userfavorite),
    path('Company/<slug>',company_page),
    # path('SendReview/<slug>',SendReview),
]