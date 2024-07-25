
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,  Addproject, orders_view, order_now, admin_panel, view_order, projects, products, members, events,delete_ordered_product, edit_ordered_product

urlpatterns = [
    path('', index, name='index'),
    path('orders/', orders_view, name='orders'),
    path('order_now/<int:order_id>/', order_now, name='order_now'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('Addproject/', Addproject, name='Addproject'),

    path('view_order/', view_order, name='view_order'),
    path('projects/', projects, name='projects'),
    path('products/', products, name='products'),
    path('members/', members, name='members'),
    path('events/', events, name='events'),


    path('delete_ordered_product/<int:product_id>/', delete_ordered_product, name='delete_ordered_product'),
    path('edit_ordered_product/<int:product_id>/', edit_ordered_product, name='edit_ordered_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
