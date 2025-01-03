from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),
    path('cupcakes/', views.cupcake_list, name='cupcake_list'),
    path('cupcakes/add/', views.add_cupcake, name='add_cupcake'),
]
