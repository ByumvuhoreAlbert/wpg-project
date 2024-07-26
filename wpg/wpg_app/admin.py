
from django.contrib import admin
from .models import ContactMessage, Order, OrderedProduct, Project

#admin.site.register(Record)
admin.site.register(ContactMessage)

admin.site.register(Order)

admin.site.register(OrderedProduct)

admin.site.register(Project)
