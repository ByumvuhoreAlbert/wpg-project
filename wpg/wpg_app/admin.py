
from django.contrib import admin
from .models import ProjectItem, Testimonial, Project,project_table

admin.site.register(ProjectItem)
admin.site.register(Testimonial)


class Project_Table_Admin(admin.ModelAdmin):
 list_display = ('title', 'height', 'width', 'date_published', 'amount')
admin.site.register( project_table)
admin.site.register(Project)




#admin.site.register(Proj)

