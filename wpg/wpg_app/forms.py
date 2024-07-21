from django import forms
<<<<<<< HEAD
from .models import ContactMessage, Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'photo', 'message']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['caption', 'description', 'price', 'photo']
=======
from .models import UploadImage
#form of adding project
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['name', 'description', 'image']
#form of deleting project
class DeleteUploadImageForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())
>>>>>>> d954deeb70cc34c4887382c2e98f17a06bcc3b1c
