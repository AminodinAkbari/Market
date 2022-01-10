from django.shortcuts import render
from Market_Product.models import Category
from Market_Cart.models import OrderDetail
# Create your views here.

def navbar(request):
    nav_categories = Category.objects.all()
    proucts_in_cart_count = (OrderDetail.objects.filter(order_id = request.user.id).count() or None)
    context = {
        'Products':'محصولات',
        'Articles':'مقالات',
        'About_us':'درباره ما',
        'Contact_us':'تماس با ما',
        'nav_category':nav_categories,
        'proucts_in_cart_count':proucts_in_cart_count
    }
    return render(request,"shared/nav.html",context)