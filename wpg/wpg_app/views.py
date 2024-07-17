# views.py
from django.shortcuts import render, get_object_or_404
#from .models import Project, project_table
def index(request):
    return render(request, 'index.html')
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def projectlist1(request):
    return render(request, 'projects/project_list1.html')

#project Tables
def projectlist2(request):
    return render(request, 'projects/project_list2.html')
def projectlist3(request):
    return render(request, 'projects/project_list3.html')
def project_table(request):
    Ptables = Project.objects.all()
    return render(request, 'projects/project_list.html', {'Ptables': Ptables})

#end of project tables
def projectlist4(request):
    return render(request, 'projects/project_list4.html')
def projectlist5(request):
    return render(request, 'projects/project_list5.html')
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})




# from django.shortcuts import render, redirect
# from .models import Proj
# from .forms import ProjectForm

# def project_list(request):
#     projects = Proj.objects.all()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('project_list')
#     else:
#         form = ProjectForm()
#     return render(request, 'projects/project_list.html', {'projects': projects, 'form': form})
