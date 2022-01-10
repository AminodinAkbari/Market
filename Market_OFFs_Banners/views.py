from django.shortcuts import render
from .models import HeaderBanner, OFFProduct_limit_time
import random

# Create your views here.
def main_off_banner(request):
    items=None
    items =HeaderBanner.objects.filter(active = True).first()
    # random_symbol = random.sample(items, 1)
    # print(random_symbol)
    
    context = {
        'ActiveBanners':items,
    }
    return render(request,'shared/HomePage_Components/OFF_banner_header.html',context)

def limit_time_discount(request):
    off_product = (OFFProduct_limit_time.objects.filter(active = True).first() or None)
    context = {'off_limit_time':off_product,}
    return render(request,'shared/limit_time.html',context)