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

<<<<<<< HEAD
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'place', 'status', 'start', 'end', 'description', 'image']
        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'}),
        }
=======
# class OrderedProductForm(forms.ModelForm):
#     class Meta:
#         model = OrderedProduct
#         fields = [
#             'full_name', 'telephone', 'address_1', 'address_2', 'address_3',
#             'address_4', 'order_name', 'price', 'date_of_completion', 'photo'
#         ]

#MEMBER FORMSfrom django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['profile_picture', 'fullname', 'telephone', 'email', 'cv', 'role', 'facebook_link', 'instagram_link', 'twitter_link']

#EVENT FORM
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_time', 'end_time', 'image', 'organizer']
>>>>>>> e9e8536114e3586496afc3389c2e0d595e05aff3
