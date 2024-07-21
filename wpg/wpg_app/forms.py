from django import forms
from .models import ContactMessage, Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'photo', 'message']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['caption', 'description', 'price', 'photo']
