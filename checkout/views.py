from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)

from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import database
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('all_products'))

    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order': order_form,
    }

    return render(request, template, context)