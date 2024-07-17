from django.db import models
class ProjectItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ProjectImage = models.ImageField(upload_to="images/")
    def __str__(self):  # sourcery skip: use-fstring-for-concatenation
        return self.title +   ' ' + self.description
    
 

class Testimonial(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
