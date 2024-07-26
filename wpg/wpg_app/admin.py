
from django.contrib import admin
from .models import ContactMessage, Member, Order, UploadImage, OrderedProduct, Event

#admin.site.register(Record)
admin.site.register(ContactMessage)

admin.site.register(Order)

admin.site.register(UploadImage)

admin.site.register(OrderedProduct)
admin.site.register(Member)
admin.site.register(Event)