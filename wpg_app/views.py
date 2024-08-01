
from asyncio import Event
from email.mime import image
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import ContactMessage, Order, OrderedProduct, Project,Member, Event
from .forms import ContactForm, OrderForms, OrderForm, OrderedProductForm, ProjectForm, MemberForm, EventForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Refresh the page to show the new message
    else:
        form = ContactForm()

    contacts = ContactMessage.objects.all()
    orders = Order.objects.all()
    projects = Project.objects.all()
    members = Member.objects.all()

    return render(request, 'index.html', {
        'form': form,
        'contacts': contacts,
        'orders': orders,
        'members': members
    })

def orders_view(request):
    if request.method == 'POST':
        form = OrderForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created successfully!')
            return redirect('admin_panel')  # Redirect to a view that lists orders or any other page
        else:
            messages.error(request, 'There was an error creating your order.')
    else:
        form = OrderForms()

    return render(request, 'orders.html', {'form': form})


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


def view_order(request):
    ordered_products = OrderedProduct.objects.all()
    return render(request, 'view_order.html', {'ordered_products': ordered_products})
def products(request):
    orders = Order.objects.all()
    return render(request, 'products.html', {'orders': orders})

def members(request):
    return render(request, 'members.html')

def events(request):
    return render(request, 'events/events.html')


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


def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        messages.success(request, 'Order deleted successfully.')
    return redirect('admin_panel')

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForms(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully.')
            return redirect('admin_panel')  # Redirect to admin_panel.html
    else:
        form = OrderForms(instance=order)

    return render(request, 'orders.html', {'form': form, 'order': order})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')  # Redirect to a page where you list projects
    else:
        form = ProjectForm()

    return render(request, 'addproject.html', {'form': form})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            return redirect('admin_panel')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('admin_panel')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member_form.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect('admin_panel')
    return render(request, 'member_confirm_delete.html', {'member': member})
# List all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

# Create a new project
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# Update an existing project
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

# Delete a project
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

#EVENTS CRUD
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})