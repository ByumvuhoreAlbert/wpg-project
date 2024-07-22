
from django.contrib import admin
from .models import ContactMessage, Order, UploadImage

#admin.site.register(Record)
admin.site.register(ContactMessage)

admin.site.register(Order)

admin.site.register(UploadImage)
