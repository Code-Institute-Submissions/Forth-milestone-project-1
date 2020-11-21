from django.shortcuts import render
from products.models import database
# Create your views here.

def index(request):
    products = database.objects.all().order_by('?')[:12]

    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)
