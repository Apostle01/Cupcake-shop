from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order, Cupcake
from .forms import CustomerForm, OrderForm, CupcakeForm


# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'orders/customer_form.html', {'form': form})


# Order Views
def order_list(request):
    orders = Order.objects.select_related('customer').all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})


# Cupcake Views
def cupcake_list(request):
    cupcakes = Cupcake.objects.select_related('order').all()
    return render(request, 'orders/cupcake_list.html', {'cupcakes': cupcakes})


def add_cupcake(request):
    if request.method == 'POST':
        form = CupcakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cupcake_list')
    else:
        form = CupcakeForm()
    return render(request, 'orders/cupcake_form.html', {'form': form})

