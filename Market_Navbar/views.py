from django.shortcuts import render
from Market_Product.models import Category
from Market_Cart.models import OrderDetail,UserFavorite
from Market_Accounts.models import Profile
# Create your views here.

def navbar(request):
    nav_categories = Category.objects.all() or None
    proucts_in_cart_count = (OrderDetail.objects.filter(order__owner_id = request.user.id).count() or 0)
    proucts_in_favorite = (UserFavorite.objects.filter(user = request.user.id).count() or 0)
    context = {
        'Products':'محصولات',
        'Articles':'مقالات',
        'About_us':'مستندات',
        'Contact_us':'تماس با ما',
        'nav_category':nav_categories,
        'proucts_in_cart_count':proucts_in_cart_count,
        'proucts_in_favorite':proucts_in_favorite,
    }
    if request.user.is_authenticated:
        obj = Profile.objects.get(user = request.user) or None
        context['current_user'] = obj

    return render(request,"shared/nav.html",context)