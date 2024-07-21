from django import forms
from .models import UploadImage
#form of adding project
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['name', 'description', 'image']
#form of deleting project
class DeleteUploadImageForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())