from django.contrib import admin
from .models import *



admin.site.register(Customer)
admin.site.register(AboutShop)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderedItems)
admin.site.register(ShippingAddress)

