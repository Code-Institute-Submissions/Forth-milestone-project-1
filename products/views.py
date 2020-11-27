from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.db.models import Count
from django.contrib import messages
from django.db.models.aggregates import Max
from django.db.models.functions import Lower
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import database

# Create your views here.

def all_products(request):
    products = database.objects.all()
    
    sort = None
    direction = None

    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'name'
                sort = sortkey
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'brand':
                sortkey = 'brand'
                sort = sortkey
            
            if sortkey == 'category':
                sortkey = 'category'
                sort = sortkey

            if sortkey == 'sub':
                sortkey = 'sub'+'_categories'
                sort = sortkey
                
                  
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                sort = sortkey
            products = database.objects.order_by(sort)
           
    
        if 'brand' in request.GET:
            brand = request.GET.get('brand')
            products = database.objects.filter(brand=brand)
            
        if 'subcategory' in request.GET:
            subcategory = request.GET.get('subcategory')
            products = database.objects.filter(sub_categories=subcategory)
        
        if 'category' in request.GET:
            category = request.GET.get('category')
            products = database.objects.filter(category=category)


        if 'q' in request.GET:
            query = request.GET.get('q')
            if not query:
                messages.error(request,("You didn't enter any search criteria!"))
                return redirect(reverse('all_products'))
            queries = Q(name__icontains=query) 
            products = database.objects.filter(queries)

        

    context = {
        'products': products,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD
        
        }
    return render(request, 'products/products2.html', context)

from django.views.generic import ListView

class blogposts(ListView):
    model = database
    paginate_by = 10

def product_detail(request, product_id, sub_categories):
    
    products = database.objects.filter(sub_categories=sub_categories).filter(~Q(id=product_id))
    product = get_object_or_404(database, pk=product_id)

    context = {
        'product': product,
        'products': products,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD
    }

    return render(request, 'products/product_detail.html', context)