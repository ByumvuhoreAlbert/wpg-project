from django import forms

from .models import ContactMessage, Order, UploadImage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'photo', 'message']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['caption', 'description', 'price', 'photo']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['name', 'description', 'image']
#form of deleting project
class DeleteUploadImageForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())

