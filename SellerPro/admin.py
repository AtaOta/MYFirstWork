from django.contrib import admin
from .models import Product, OrderedItem, Order


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedItem)

