from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.aggregates import Max
from django.db.models.functions import Lower
from django.db.models import Q
from .models import database
from .forms import ProductForm

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
            products = database.objects.order_by(sortkey)
           
    
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
        'products': products
        }
    return render(request, 'products/products2.html', context)



def product_detail(request, product_id, sub_categories):
    
    products = database.objects.filter(sub_categories=sub_categories).filter(~Q(id=product_id))
    product = get_object_or_404(database, pk=product_id)

    context = {
        'product': product,
        'products': products
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product_detail', args=[product.id, product.sub_categories]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    product = get_object_or_404(database, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id, product.sub_categories]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(database, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('all_products'))