from django import forms
from .models import Order
from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'second_name', 'email', 'phone_number','street_address',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'second_name': 'Second Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County, State or Locality',
            'country': 'Country',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'