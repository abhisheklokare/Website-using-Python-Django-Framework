from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    name = forms.CharField(label = "Name*", max_length = 100,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Name', 'type' : 'text'}))
    email = forms.EmailField(label = "E-mail*", max_length = 100, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'E-Mail Id', 'type' : 'email'}))
    mobileNum = forms.CharField(label = "Phone Number*", max_length= 25, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Phone Number', 'type' : 'text'}))
    roofType = forms.CharField(label = "Roof Type*", max_length = 50, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Roof Type', 'type' : 'text'}))
    roofHeight = forms.CharField(label = "Roof Height*", max_length = 20, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Roof Height', 'type' : 'text'}))
    electricityBoard = forms.CharField(label = "Electricity Board*", max_length = 100, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Electricity Board', 'type' : 'text'}))
    otherDetails = forms.CharField(label = "Any Other Details*",
                          widget=forms.Textarea(attrs= {'placeholder' : 'Other Details'}))
    address = forms.CharField(label = "Address*", max_length = 300,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Address', 'type' : 'text'}))
    latitude = forms.CharField(label = "Latitude*", max_length = 20, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Latitude', 'type' : 'text', 'disabled' : ''}))
    longitude = forms.CharField(label = "Longitude*", max_length = 20, required = True,
                          widget = forms.TextInput(attrs = {'placeholder' : 'Longitude', 'type' : 'text', 'disabled' : ''}))
