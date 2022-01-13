from django.shortcuts import render
from Market_Product.models import *
from Market_OFFs_Banners.models import HeaderBanner
def home_page(request):
    
    # products = Product.objects.all()
    context = {
        
        'category_btn':'محصولات',
        # 'products':products
    }
    return render(request,"index.html",context)

def SideItems(request):
    Side_all_categories = Category.objects.all()
    if Side_all_categories:
        context= {
            'side_all_categories':Side_all_categories,
        }
        return render(request,'shared/ProductsList_Side.html',context)

# def some_view(request):
#     if request.POST:
#         form = CaptchaTestForm(request.POST)

#         # Validate the form: the captcha field will automatically
#         # check the input
#         if form.is_valid():
#             human = True
#     else:
#         form = CaptchaTestForm()

#     return render(request, 'accounts/login.html', {'form': form})