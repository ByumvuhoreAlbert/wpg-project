from . import views
from django.contrib import admin
from django.urls import path
from .views import index, testimonial_view


urlpatterns = [
path('', views.index, name='index'),
path('project_list',views.project_list, name='project_list'),

path('item/<int:pk>/',views.project_detail, name='project_detail'),
path('testimonial_view/', testimonial_view, name='testimonial_view'),
path('testimonials/', testimonial_view, name='testimonial_view'),

path('projectlist1',views.projectlist1, name='projectlist1'),
path('projectlist2',views.projectlist2, name='projectlist2'),
path(' project_table',views. project_table, name=' project_table'),
path('projectlist3',views.projectlist3, name='projectlist3'),
path('projectlist4',views.projectlist4, name='projectlist4'),
path('projectlist5',views.projectlist5, name='projectlist5'),
path('projects/<int:project_id>/',views.project_detail, name='project_detail'),

 ]


# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.project_list, name='project_list'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

