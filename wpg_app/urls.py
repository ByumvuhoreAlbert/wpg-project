
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import event_delete, event_detail, event_edit, event_list, event_new, index, order_now, admin_panel, project_create, project_delete, project_list, project_update, view_order, products, members, add_project, delete_ordered_product, edit_ordered_product, orders_view, delete_order, edit_order, member_list,member_detail,member_create,member_update,member_delete
urlpatterns = [
    path('', index, name='index'),
    path('orders/', orders_view, name='orders'),
    path('order_now/<int:order_id>/', order_now, name='order_now'),
    path('admin_panel/', admin_panel, name='admin_panel'),

    path('view_order/', view_order, name='view_order'),
    # path('projects/', projects, name='projects'),
    path('products/', products, name='products'),
    path('members/', members, name='members'),
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
    #projects
    path('project_list', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/update/', project_update, name='project_update'),
    path('<int:pk>/delete/', project_delete, name='project_delete'),
    #EVENTS CRUD
    path('event_list', event_list, name='event_list'),
    path('<int:pk>/',event_detail, name='event_detail'),
    path('new/', event_new, name='event_new'),
    path('<int:pk>/edit/', event_edit, name='event_edit'),
    path('<int:pk>/delete/', event_delete, name='event_delete'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
