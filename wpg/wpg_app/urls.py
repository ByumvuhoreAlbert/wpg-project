# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('Addproject/', views.Addproject, name='Addproject'),
    path('', views.index, name='index'),
   # path('delete_upload_image/', views.delete_upload_image_view, name='delete_upload_image'),
]
