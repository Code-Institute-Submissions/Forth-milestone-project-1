from django.shortcuts import render
from django.conf import settings
from products.models import database
# Create your views here.

def index(request):
    products = database.objects.all().order_by('?')[:12]

    context = {
        'products': products,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }
    return render(request, 'home/index.html', context)
