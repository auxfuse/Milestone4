from django.contrib import admin
from .models import Order, OrderLineItem

# Registered Models for Admin dashboard
admin.site.register(Order)
admin.site.register(OrderLineItem)
