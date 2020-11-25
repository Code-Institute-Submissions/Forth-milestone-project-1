from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count
from django.db.models.aggregates import Max
from .models import database

# Create your views here.

def all_products(request):
    products = database.objects.all()
    
    if 'brand' in request.GET:
        brand = request.GET.get('brand')
        products = database.objects.filter(brand=brand)
    
    if 'subcategory' in request.GET:
        subcategory = request.GET.get('subcategory')
        products = database.objects.filter(sub_categories=subcategory)
    
    if 'category' in request.GET:
        category = request.GET.get('category')
        products = database.objects.filter(category=category)
    context = {
        'products': products
        }
    return render(request, 'products/products2.html', context)

