from django.shortcuts import redirect, render
from .forms import NewOrderForm
from .models import *
from Market_Product.models import Product
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def Cart(request):
    items = OrderDetail.objects.filter(order_id = request.user.id)
    open_order:Order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    context ={'items':items,'this_order':open_order}

    # if items:
    #     context['total'] = items.get_total_price()

    return render(request,'shared/Cart.html',context)

@login_required(login_url='/login')
def add_to_order_detail(request,slug):
    Form = NewOrderForm(request.POST or None)
    print(Form)
    if Form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        print(order)
        count = Form.cleaned_data['count']
        
        if count < 0:
            count = 1
        product = Product.objects.get_by_slug(slug)
        print(product)
        
        if order is None:
            print("order is None")
            order = Order.objects.create(owner_id=request.user.id,is_paid=False)
        
        order.orderdetail_set.create(product_id=product.id,count=count,price=product.price - product.off_sale)    

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
    order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    
    if order is None:
        print("order is None")
        order = Order.objects.create(owner_id=request.user.id,is_paid=False)

    product = Product.objects.get_by_slug(slug)
    order.userfavorite_set.create(favorite_id=product.id,user_id = order.owner_id)
    return redirect('/')
