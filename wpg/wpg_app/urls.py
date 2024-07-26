
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/',views. orders_view, name='orders'),
    path('order_now/<int:order_id>/',views.order_now, name='order_now'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('Addproject/', views.Addproject, name='Addproject'),

    path('view_order/', views.view_order, name='view_order'),
    path('projects/', views.projects, name='projects'),
    path('products/', views.products, name='products'),
    path('members/',views.members, name='members'),
    path('events/', views.events, name='events'),
    path('delete_ordered_product/<int:product_id>/', views.delete_ordered_product, name='delete_ordered_product'),
    path('edit_ordered_product/<int:product_id>/',views. edit_ordered_product, name='edit_ordered_product'),
    #Member CRUD methods
    path('member_list', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_create, name='member_create'),
    path('member/<int:pk>/edit/', views.member_update, name='member_update'),
    path('member/<int:pk>/delete/', views.member_delete, name='member_delete'),
    
    #EVENT methods
    path('event_list/', views.event_list, name='event_list'),
    path('event_detail/<int:pk>/', views.event_detail, name='event_detail'),
    path('event_create/', views.event_create, name='event_create'),
    path('events/<int:pk>/edit/', views.event_update, name='event_update'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

