from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Order(models.Model):
    caption = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='orders/')

    def __str__(self):
        return self.caption


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=100)  # District
    address_2 = models.CharField(max_length=100)  # Sector
    address_3 = models.CharField(max_length=100)  # Cell
    address_4 = models.CharField(max_length=100)  # Village
    completed = models.DateField(null=True, blank=True)
    products = models.CharField(max_length=100)
    sells = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='ordered_products/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.order.caption}"

class Project(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title
