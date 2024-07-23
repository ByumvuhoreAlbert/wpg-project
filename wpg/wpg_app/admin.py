
from django.contrib import admin
from .models import ContactMessage, Order, UploadImage, OrderedProduct

#admin.site.register(Record)
admin.site.register(ContactMessage)

admin.site.register(Order)

admin.site.register(UploadImage)

admin.site.register(OrderedProduct)
