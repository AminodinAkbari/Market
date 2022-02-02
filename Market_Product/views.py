from django.shortcuts import render
from Market.views import home_page
from django.db.models import F
from django.db.models import Count
from django.views.generic import ListView
import random
from django.http import Http404
from django.contrib import messages

# from Market_Cart.forms import NewOrderForm
from .forms import ReviewForm
from Market_Product.models import *
from Market_Cart.models import UserFavorite
from Market.tools import debugger

from Market_Cart.forms import NewOrderForm

from .utils import get_rate_avg

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FullSerializer , ProductMinimalSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
import django_filters
from .permissions import Safe

class AllProducts(ListView):
    template_name = 'products_templates/All_Products(ListView).html'
    paginate_by = 8
    def get_queryset(self):
        return Product.objects.filter(active = True)

class AllProductsByCategory(ListView):
    template_name = 'products_templates/All_Products(ListView).html'
    paginate_by = 8
    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(url_name__iexact=category_name).first()
        if category is None:
            raise Http404('یافت نشد')
        return Product.objects.get_products_by_category(category_name)

def categories(request):
    # count_ = Category.objects.all().annotate(num_products = Count('product'))[:4]
    items = list(Category.objects.all().annotate(num_products = Count('product')))
    header_categories = random.sample(items, 4)
    middle_categories = random.sample(items, 3)
    botton_categories = random.sample(items, 4)
    context = {
        'category_btn':'مشاهده محصولات',
        'count':header_categories,
        'middle_categories':middle_categories,
        'botton_categories':botton_categories,
    }

    return render(request,'shared/HomePage_Components/Header_Categories.html',context)

def home_products(request):
    products = Product.objects.filter(active = True).order_by('date').annotate(offer=F('price')-F('off_sale'))[:10]
    context = {
        "products":products,
        
    }
    return render(request,'shared/sliders/product_slider.html',context)


def pick_randomly(request):
        items = list(Product.objects.filter(active = True))
        random_symbol = random.sample(items, 6)
        context = {
            'item':random_symbol
        }
        return render(request,'products_templates/Random_products.html',context)

# class ProductDetailView(DetailView):
#      queryset = Product
#      template_name = 'products_templates/ProductDetail.html'
    # template =
    
def product_detail(request, slug):
    qs = Product.objects.get(slug=slug)
    splited_features = qs.featuers.split("،")
    img = Images.objects.filter(product = qs)
    related_products = Product.objects.get_queryset().filter(tags__product=qs).exclude(id=qs.id).distinct()[:8] 
    comments = Review.objects.filter(product=qs.id,status = 'True')
    if comments.count() > 1:
        rate_avg = get_rate_avg(comments)
    else:
        rate_avg = None

    # rate = comments.rate
    all_comments_for_this_qs = Review.objects.filter(product=qs.id ,status = True).count()
    form = ReviewForm(request.POST or None)
    # current_user = Profile.objects.get(user_id=request.user.id)
    new_form_order = NewOrderForm(request.POST or None)
    if form.is_valid():
        rate = form.cleaned_data.get('rate')
        comment = form.cleaned_data.get('comment')
        # print(rate,comment)

        product = Product.objects.get(slug = slug)
        user = User.objects.get(id=request.user.id)

        if not Review.objects.filter(user=user,product=product):
            Review.objects.create(rate=rate,comment=comment,product=product,user=user)
            messages.success(request, 'Form submission successful')
            

    if qs is None and img is None:
        return home_page



    context = {
        "item":qs,
        'img':img,
        'related':related_products,
        'comments':comments,
        'rate_avg':rate_avg,
        'count_comments':all_comments_for_this_qs,
        'form':form,
        # 'this_user':current_user,
        'Form':new_form_order,
        'featuers':splited_features,
        }


    return render(request,'products_templates/ProductDetail.html',context)


class ProductSearch(ListView):
    template_name = 'products_templates/All_Products(ListView).html'
    paginate_by = 4

    def get_queryset(self):
        request=self.request
        print(request.GET)
        our_query = request.GET.get('q')
        if our_query is not None:
            return Product.objects.search(our_query)
        return Product.objects.all()


def userfavorite(request):
    favorite = UserFavorite.objects.filter(user = request.user.id)
    return render(request,'user/Favorites.html',{'favorite':favorite})

def company_page(request,slug):
    company = Product.objects.get(slug = slug)
    return render(request,'products_templates/Company.html',{'company':company})


    # ----------- Django Rest FrameWork --------------

@api_view(['GET'])
def product_list(request):
    qs = Product.objects.all()
    serializer = FullSerializer(qs , many = True)
    return Response(serializer.data)

class ProductUnsafeMethodes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = FullSerializer
    permission_classes = ((Safe,))

class ProductSizes(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FullSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sizes']

class ProductPriceFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price']

class ProductPriceRange(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FullSerializer
    filter_class = ProductPriceFilter