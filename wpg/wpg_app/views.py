from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
#from .models import ProjectItem
from .models import Testimonial
from .forms import TestimonialForm


def index(request):
    return render(request, 'index.html')
    
def project_list(request):
    items = ProjectItem.objects.all()
    return render(request, 'projects/project_list.html', {'items': items})

def project_detail(request, pk):
    item =get_object_or_404(ProjectItem, pk=pk)
    return render(request, 'projects/project_detail.html', {'item': item})

def index(request):
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    return render(request, 'index.html', {'testimonials': testimonials})

def testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()  # Save the testimonial to the database
            return redirect('index')  # Redirect to a success page or similar
    else:
        form = TestimonialForm()
    
    return render(request, 'index.html', {'form': form})




    
