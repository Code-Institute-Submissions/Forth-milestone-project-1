from django.shortcuts import render
from django.db.models import Count
from django.db.models.aggregates import Max
from .models import database

# Create your views here.

def all_products(request):  
    products = database.objects.all()
    counts = database.objects.values('sub_categories').annotate(count_subcategories=Count('name')).order_by()
    images = database.objects.values('sub_categories').annotate(latest_date=Max('url1')).order_by()
    context = {
        'products': products,
        'counts': counts,
        'images': images
    }
    return render(request, 'products/products.html', context)
