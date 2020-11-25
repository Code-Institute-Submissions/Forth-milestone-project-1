from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count
from django.db.models.aggregates import Max
from .models import database

# Create your views here.

def all_products(request):
    products = database.objects.all()
    

    if request.GET: 
        brand = request.GET.get("brand")
        category = request.GET.get("category")
        products = database.objects.filter(category=category)
        products = database.objects.filter(brand=brand)
        products = database.objects.filter(sub_categories=brand)
        
       
        
    
    
    context = {
        'products': products
        }
    return render(request, 'products/products2.html', context)

