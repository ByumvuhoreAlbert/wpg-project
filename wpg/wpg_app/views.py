
from django.shortcuts import get_object_or_404, render, redirect
from .models import ContactMessage, Order, UploadImage
from .forms import ContactForm, OrderForm

def index(request):
    # Fetch messages for display on the index page
    messages = ContactMessage.objects.all()
    orders = Order.objects.all()  # Fetch orders for display on the index page
    return render(request, 'index.html', {'messages': messages, 'orders': orders})

def submit_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'submit_message.html', {'form': form})

def orders_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'orders.html', {'form': form})


def order_now(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data here
            # For example, save the order or send a confirmation email
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

# views.py
from django.shortcuts import render

def view_order(request):
    return render(request, 'view_order.html')

def add_products(request):
    return render(request, 'add_products.html')

def add_new(request):
    return render(request, 'add_new.html')

def add_event(request):
    return render(request, 'add_event.html')
    

# views.py

from django.shortcuts import render, redirect
from .models import UploadImage
from .forms import UploadImageForm


def index(request):
    images = UploadImage.objects.all()
    return render(request, 'index.html', {'images': images})

def Addproject(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadImageForm()
    return render(request, 'Addproject.html', {'form': form})





