
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import admin_panel, index,  Addproject, orders_view, order_now, upload_image #submit_message, admin_panel,view_order, add_new, add_event, add_products,

urlpatterns = [
    path('', index, name='index'),
    #path('submit_message/', submit_message, name='submit_message'),
    path('orders/', orders_view, name='orders'),
    path('order_now/<int:order_id>/', order_now, name='order_now'),
    path('admin_panel/', admin_panel, name='admin_panel'),

    # path('view-order/', view_order, name='view_order'),
    # path('add-new/', add_new, name='add_new'),
    # path('add-products/', add_products, name='add_products'),

    # #Add_Event
    # path('add-event/', add_event, name='add_event'),

#Add_Project
    path('Addproject/', Addproject, name='Addproject'),

    #Static and media URL patterns (if needed),
    # path('static/<path:path>/', static_serve, name='static'),
    # path('media/<path:path>/', media_serve, name='media'),
    path('upload/',upload_image, name='upload_image'),
    path('image/<int:image_id>/', views.view_image, name='view_image'),
    path('image/<int:image_id>/update/', views.update_image, name='update_image'),
    path('image/<int:image_id>/delete/', views.delete_image, name='delete_image'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
