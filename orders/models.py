from django.db import models
from decimal import Decimal


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)  # Added Zipcode/Postcode field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    DELIVERY_TYPE_CHOICES = [
        ('Pickup', 'Pickup'),
        ('Delivery', 'Delivery'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES)
    fulfillment_date = models.DateField()
    fulfillment_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"


class Cupcake(models.Model):
    FLAVOR_CHOICES = [
        ('Vanilla', 'Vanilla'),
        ('Chocolate', 'Chocolate'),
        ('Red Velvet', 'Red Velvet'),
        ('Strawberry', 'Strawberry'),
    ]

    ICING_CHOICES = [
        ('Vanilla', 'Vanilla'),
        ('Buttercream', 'Buttercream'),
        ('Chocolate', 'Chocolate'),
        ('Cream Cheese', 'Cream Cheese'),
    ]

    COLORS = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Pink', 'Pink'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cupcakes')
    flavor = models.CharField(max_length=50, choices=FLAVOR_CHOICES)
    icing_flavor = models.CharField(max_length=50, choices=ICING_CHOICES)
    cupcake_color = models.CharField(max_length=20, choices=COLORS, blank=True, null=True)
    icing_color = models.CharField(max_length=20, choices=COLORS, blank=True, null=True)
    decorations = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    image = models.ImageField(upload_to='images/', default='images/default_cupcake.jpg')  # Images will be stored in 'media/images/'

    def __str__(self):
        return f"Cupcake #{self.id} for Order #{self.order.id} - {self.flavor}"
