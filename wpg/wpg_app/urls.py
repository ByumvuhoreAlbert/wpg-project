from . import views
from django.contrib import admin
from django.urls import path
#from .views import index #contacts_view


urlpatterns = [
path('', views.index, name='index'),
#path('contacts_view/', contacts_view, name='contacts_view'),

#path(' project_table',views. project_table, name=' project_table'),


 ]



