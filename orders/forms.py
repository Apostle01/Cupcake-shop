from django import forms
from .models import Customer, Order, Cupcake


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street_address', 'city']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter customer email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g. +123456789'}),
            'street_address': forms.Textarea(attrs={'rows': 2}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'delivery_type', 'fulfillment_date', 'fulfillment_time', 'notes']
        widgets = {
            'fulfillment_date': forms.DateInput(attrs={'type': 'date'}),
            'fulfillment_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }


class CupcakeForm(forms.ModelForm):
    class Meta:
        model = Cupcake
        fields = ['order', 'flavor', 'icing_flavor', 'cupcake_color', 'icing_color', 'decorations']
        widgets = {
            'decorations': forms.Textarea(attrs={'rows': 2}),
        }
