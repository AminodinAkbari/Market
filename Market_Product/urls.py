from django.urls import path
from Market_Product.views import *
from Market.views import SideItems


app_name = 'Market'
urlpatterns = [
    path('product_detail/<slug>',product_detail),
    path('AllProducts',AllProducts.as_view(),name='AllProducts'),
    path('categories/<category_name>',AllProductsByCategory.as_view()),
    path('search',ProductSearch.as_view()),
    path('AllProducts',SideItems),
    path('favorites',userfavorite),
    path('Company/<slug>',company_page),
    # DJANGO REST API
    path('product_list',product_list),
    path('product_manage/<int:pk>',ProductUnsafeMethodes.as_view()),
    path('product_price',ProductPriceRange.as_view()),
    path('product_sizes',ProductSizes.as_view()),
]