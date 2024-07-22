
# models.py
from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname


class Order(models.Model):
    caption = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.caption



class UploadImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    

