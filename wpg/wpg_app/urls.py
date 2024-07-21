from django.urls import path
from .views import index, submit_message, orders_view, order_now, admin_panel,view_order, add_new, add_event, add_products

urlpatterns = [
    path('', index, name='index'),
    path('submit_message/', submit_message, name='submit_message'),
    path('orders/', orders_view, name='orders'),
    path('order_now/<int:order_id>/', order_now, name='order_now'),
    path('admin_panel/', admin_panel, name='admin_panel'),

    path('view-order/', view_order, name='view_order'),
    path('add-new/', add_new, name='add_new'),
    path('add-products/', add_products, name='add_products'),
    path('add-event/', add_event, name='add_event'),
]
