
from email.mime import image
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import ContactMessage, Order, UploadImage, UploadImage, OrderedProduct, UploadImage
from .forms import ContactForm, OrderForms, OrderForm, UploadImageForm, OrderedProductForm, UploadImageForm

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
        form = OrderForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error placing your order.')
    else:
        form = OrderForms()

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



def admin_panel(request):
     return render(request, 'admin_panel.html')




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


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page or another view
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})

def view_order(request):
    ordered_products = OrderedProduct.objects.all()
    return render(request, 'view_order.html', {'ordered_products': ordered_products})


def projects(request):
    return render(request, 'projects.html')

def products(request):
    return render(request, 'products.html')

def members(request):
    return render(request, 'members.html')

def events(request):
    return render(request, 'events.html')


def delete_ordered_product(request, product_id):
    product = get_object_or_404(OrderedProduct, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_panel')
    return redirect('view_order')



def edit_ordered_product(request, product_id):
    product = get_object_or_404(OrderedProduct, id=product_id)
    if request.method == 'POST':
        form = OrderedProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_order')
    else:
        form = OrderedProductForm(instance=product)

    return render(request, 'edit_ordered_product.html', {'form': form, 'product': product})
