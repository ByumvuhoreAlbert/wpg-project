
from email.mime import image
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import ContactMessage, Order, UploadImage, UploadImage
from .forms import ContactForm, OrderForm, UploadImageForm

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
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to the index page after successful form submission
    else:
        form = OrderForm(initial={
            'caption': order.caption,
            'description': order.description,
            'price': order.price,
            'photo': order.photo
        })

    return render(request, 'order_now.html', {'order': order, 'form': form})

def admin_panel(request):
     return render(request, 'admin_panel.html')
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
from django.shortcuts import render
from .models import UploadImage

def update_project(request, image_id):
    image = UploadImage.objects.get(pk=image_id)
    # Update fields as needed
    image.name = 'Updated Name'
    image.description = 'Updated Description'
    image.category = 'Updated Category'
    image.save()
    return render(request, 'update_success.html', {'image': image})







#CRUD methods
from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadImage
from .forms import UploadImageForm

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page or another view
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})

def view_image(request, image_id):
    image = get_object_or_404(UploadImage, pk=image_id)
    return render(request, 'view_image.html', {'image': image})

def update_image(request, image_id):
    image = get_object_or_404(UploadImage, pk=image_id)
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('view_image', image_id=image_id)  # Redirect to view image after update
    else:
        form = UploadImageForm(instance=image)
    return render(request, 'update_image.html', {'form': form})

def delete_image(request, image_id):
    image = get_object_or_404(UploadImage, pk=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('image_deleted')  # Redirect to a success page or another view
    return render(request, 'delete_image.html', {'image': image})
