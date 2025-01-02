from django.contrib import admin
from .models import Customer, Order, Cupcake


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Display key fields for customer management
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'street_address', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('city',)
    ordering = ('last_name', 'first_name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Display essential details for each order
    list_display = ('id', 'customer', 'order_date', 'delivery_type', 'fulfillment_date', 'fulfillment_time')
    search_fields = ('customer__first_name', 'customer__last_name', 'id')
    list_filter = ('delivery_type', 'order_date', 'fulfillment_date')
    ordering = ('-order_date',)
    date_hierarchy = 'order_date'


@admin.register(Cupcake)
class CupcakeAdmin(admin.ModelAdmin):
    # Display details for each cupcake in an order
    list_display = ('id', 'order', 'flavor', 'icing_flavor', 'cupcake_color', 'icing_color', 'decorations')
    search_fields = ('flavor', 'icing_flavor', 'order__id')
    list_filter = ('flavor', 'icing_flavor', 'cupcake_color', 'icing_color')
    ordering = ('order', 'id')
