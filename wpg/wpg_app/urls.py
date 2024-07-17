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
]
