from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')  # Ensure you have image field to display

    def __str__(self):
        return self.title

class  project_table(models.Model):
    title = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    date_published = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


# from django.db import models

# class Proj(models.Model):
#     title = models.CharField(max_length=100)
#     height = models.CharField(max_length=10)
#     width = models.CharField(max_length=10)
#     date_published = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='project_images/', null=True, blank=True)

#     def __str__(self):
#         return self.title
