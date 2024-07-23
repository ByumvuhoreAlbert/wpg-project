
from email.mime import image
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import ContactMessage, Order, UploadImage, UploadImage, OrderedProduct
from .forms import ContactForm, OrderForm, UploadImageForm, OrderedProductForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Refresh the page to show the new message
    else:
        form = ContactForm()

    # Fetch messages and orders for display
    contact_messages = ContactMessage.objects.all()
    orders = Order.objects.all()

    return render(request, 'index.html', {
        'contact_messages': contact_messages,
        'orders': orders,
        'form': form
    })


def orders_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error placing your order.')
    else:
        form = OrderForm()

    orders = Order.objects.all()  # Retrieve all orders
    return render(request, 'orders.html', {'form': form, 'orders': orders})


def order_now(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, request.FILES, instance=order)
        ordered_product_form = OrderedProductForm(request.POST, request.FILES)
        if order_form.is_valid() and ordered_product_form.is_valid():
            order_form.save()
            ordered_product = ordered_product_form.save(commit=False)
            ordered_product.order = order
            # If there's no photo in the form, use the order's photo
            if not ordered_product.photo:
                ordered_product.photo = order.photo
            ordered_product.save()
            return redirect('index')  # Redirect to the index page after successful form submission
    else:
        order_form = OrderForm(instance=order)
        ordered_product_form = OrderedProductForm()

    return render(request, 'order_now.html', {
        'order': order,
        'order_form': order_form,
        'ordered_product_form': ordered_product_form
    })

# def order_now(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#
#     if request.method == 'POST':
#         order_form = OrderForm(request.POST, request.FILES, instance=order)
#         ordered_product_form = OrderedProductForm(request.POST)
#         if ordered_product_form.is_valid():
#             ordered_product = ordered_product_form.save(commit=False)
#             ordered_product.order = order
#             ordered_product.save()
#             return redirect('index')  # Redirect to the index page after successful form submission
#     else:
#         order_form = OrderForm(instance=order)
#         ordered_product_form = OrderedProductForm()
#
#     return render(request, 'order_now.html', {
#         'order': order,
#         'order_form': order_form,
#         'ordered_product_form': ordered_product_form
#     })

# def admin_panel(request):
#     return render(request, 'admin_panel.html')
#
# # views.py
# from django.shortcuts import render
#
# def view_order(request):
#     return render(request, 'view_order.html')
#
# def add_products(request):
#     return render(request, 'add_products.html')
#
# def add_new(request):
#     return render(request, 'add_new.html')
#
# def add_event(request):
#     return render(request, 'add_event.html')


#Add_PROJECT IN INDEX
def Addproject(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadImageForm()
    return render(request, 'Addproject.html', {'form': form})

def index(request):
    contact_messages = ContactMessage.objects.all()
    orders = Order.objects.all()
    images = UploadImage.objects.all()
    return render(request, 'index.html', {
        'contact_messages': contact_messages,
        'orders': orders,
        'images': images
    })
