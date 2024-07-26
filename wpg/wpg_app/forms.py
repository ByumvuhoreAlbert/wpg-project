from django import forms
from .models import ContactMessage, Order, OrderedProduct, Project

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'photo', 'message']

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['caption', 'description', 'price', 'photo']


#form of deleting project
class DeleteUploadImageForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['photo']


class OrderedProductForm(forms.ModelForm):
    class Meta:
        model = OrderedProduct
        fields = [
            'full_name', 'telephone', 'address_1', 'address_2',
            'address_3', 'address_4', 'completed', 'products', 'sells'
        ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'place', 'status', 'start', 'end', 'description', 'image']
        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'}),
        }
