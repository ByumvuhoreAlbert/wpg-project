from django.shortcuts import get_object_or_404, render
from .models import ProjectItem
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def project_list(request):
    items = ProjectItem.objects.all()
    return render(request, 'projects/project_list.html', {'items': items})

def project_detail(request, pk):
    item =get_object_or_404(ProjectItem, pk=pk)
    return render(request, 'projects/project_detail.html', {'item': item})
    
