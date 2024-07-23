
# models.py
from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname


# class Order(models.Model):
#     caption = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     photo = models.ImageField(upload_to='orders/', blank=True, null=True)
#
#     def __str__(self):
#         return self.caption



class UploadImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    caption = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='orders/')

    def __str__(self):
        return self.caption

# class OrderProduct(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)
#     address_1 = models.CharField(max_length=100)  # District
#     address_2 = models.CharField(max_length=100)  # Sector
#     address_3 = models.CharField(max_length=100)  # Cell
#     address_4 = models.CharField(max_length=100)  # Village
#     products = models.CharField(max_length=100)
#     sells = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='ordered_products/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.full_name} - {self.order.caption}"

# class OrderedProduct(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)
#     address_1 = models.CharField(max_length=100)  # District
#     address_2 = models.CharField(max_length=100)  # Sector
#     address_3 = models.CharField(max_length=100)  # Cell
#     address_4 = models.CharField(max_length=100)  # Village
#     date_of_completion = models.DateField()
#     photo = models.ImageField(upload_to='ordered_products/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.full_name} - {self.order.caption}"

class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=100)  # District
    address_2 = models.CharField(max_length=100)  # Sector
    address_3 = models.CharField(max_length=100)  # Cell
    address_4 = models.CharField(max_length=100)  # Village
    products = models.CharField(max_length=100)
    sells = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='ordered_products/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.order.caption}"
