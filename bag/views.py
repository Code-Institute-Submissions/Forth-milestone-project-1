from django.shortcuts import render
from products.models import database
# Create your views here.

def view_bag(request):
    
    return render(request, 'bag/bag.html')
