from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
path('', views.index, name='index'),
path('project_list',views.project_list, name='project_list'),
path('item/<int:pk>/',views.project_detail, name='project_detail'),
]
