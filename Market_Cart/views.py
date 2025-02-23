from django.shortcuts import redirect, render
from .forms import NewOrderForm
from .models import *
from Market_Product.models import Product
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def Cart(request):
    open_order:Order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
    items = (OrderDetail.objects.filter(order_id = open_order or None))
    context ={'items':items,'this_order':open_order}


    return render(request,'shared/Cart.html',context)

@login_required(login_url='/login')
def add_to_order_detail(request,slug):
    Form = NewOrderForm(request.POST or None)

    size = request.POST['size'] or None
    color = request.POST['color'] or None
    print(color)

    if Form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
        print(order)
        count = Form.cleaned_data['count'] or None
        
        if count < 0:
            count = 1
        product = Product.objects.get_by_slug(slug) or None
        print(product)
        
        if order is None:
            print("order is None")
            order = Order.objects.create(owner_id=request.user.id,is_paid=False)
        
        order.orderdetail_set.create(product_id=product.id,count=count,price=product.price - product.off_sale,size = size,color = color)    

        return redirect('/')
    else:
        print("Form is not valid")
        return redirect('/Hichi')

@login_required(login_url='/login')
def remove_item_fromcart(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/cart')
    raise Http404()


@login_required(login_url='/login')
def add_to_favorite(request,slug):
    order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
    print(order.owner_id)

    if order is None:
        print("order is None")
        order = Order.objects.create(owner_id=request.user.id,is_paid=False)

    product = Product.objects.get_by_slug(slug)
    UserFavorite.objects.create(favorite_id=product.id,user = request.user.id)
    return redirect('/')
    
@login_required(login_url='/login')
def remove_item_favorite(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = UserFavorite.objects.get_queryset().get(id=detail_id) or None
        if order_detail is not None:
            order_detail.delete()
            return redirect('/favorites')
    raise Http404()