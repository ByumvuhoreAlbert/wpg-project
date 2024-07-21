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

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import UploadImage
from .forms import DeleteUploadImageForm
#Deleting project
# def delete_upload_image_view(request):
#     if request.method == 'POST':
#         form = DeleteUploadImageForm(request.POST)
#         if form.is_valid():
#             image_id = form.cleaned_data['image_id']
#             image = get_object_or_404(UploadImage, id=image_id)
#             image.delete()
#             return redirect('deleteproject')  # Redirect to the gallery or another page
#     return HttpResponse(status=405)  # Method not allowed



