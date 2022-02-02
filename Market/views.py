from django.shortcuts import render
from Market_Product.models import *

def home_page(request):
    context = {
        'category_btn':'محصولات',
    }
    
        
    return render(request,"index.html",context)

def SideItems(request):
    Side_all_categories = Category.objects.all() or None
    if Side_all_categories:
        context= {
            'side_all_categories':Side_all_categories,
        }
        return render(request,'shared/ProductsList_Side.html',context)