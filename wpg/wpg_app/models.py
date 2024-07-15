from django.db import models
class ProjectItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ProjectImage = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.title +   ' ' + self.description