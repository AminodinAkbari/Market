from django import template
from django.db.models import Count
from Market_Product.models import Category,Product
import random

register = template.Library()

@register.inclusion_tag('products_templates/Random_products.html')
def random_product():
    items = list(Product.objects.filter(active = True))
    random_symbol = random.sample(items, 6)
    return {'item':random_symbol}

@register.inclusion_tag('./shared/HomePage_Components/Header_Categories.html')
def random_categories():
    items = list(Category.objects.all().annotate(num_products = Count('product')))
    header_categories = random.sample(items, 4)
    return {'count':header_categories,'category_btn':'مشاهده محصولات'}