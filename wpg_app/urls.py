
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, order_now, admin_panel, view_order, projects, products, members, add_project, delete_ordered_product, edit_ordered_product, orders_view, delete_order, edit_order, member_list,member_detail,member_create,member_update,member_delete, add_event, event_list, event_update,event_delete, login_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('orders/', orders_view, name='orders'),
    path('order_now/<int:order_id>/', order_now, name='order_now'),
    path('admin_panel/', admin_panel, name='admin_panel'),

    path('view_order/', view_order, name='view_order'),
    path('projects/', projects, name='projects'),
    path('products/', products, name='products'),
    path('members/', members, name='members'),
    path('add_event/', add_event, name='add_event'),
    path('event_list/', event_list, name='event_list'),
    path('add_project/', add_project, name='add_project'),


    path('delete_ordered_product/<int:product_id>/', delete_ordered_product, name='delete_ordered_product'),
    path('edit_ordered_product/<int:product_id>/', edit_ordered_product, name='edit_ordered_product'),
    path('orders/delete/<int:order_id>/', delete_order, name='delete_order'),
    path('orders/edit/<int:order_id>/', edit_order, name='edit_order'),

    #Member CRUD methods
    path('member_list', member_list, name='member_list'),
    path('member/<int:pk>/', member_detail, name='member_detail'),
    path('member/new/', member_create, name='member_create'),
    path('member/<int:pk>/edit/', member_update, name='member_update'),
    path('member/<int:pk>/delete/', member_delete, name='member_delete'),


    path('events/<int:pk>/edit/', event_update, name='event_update'),
    path('events/<int:pk>/delete/', event_delete, name='event_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
