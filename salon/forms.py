from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = CustomerBook
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'hair_service':forms.Select(attrs={'class':'form-control'}),
            'nails_service':forms.Select(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class NailUpdateForm(ModelForm):
    class Meta:
        model = NailServices
        fields = '__all__'
        widgets = {
            'nailservice_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }

class HairUpdateForm(ModelForm):
    class Meta:
        model = HairServices
        fields = '__all__'
        widgets = {
            'hairservice_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        widgets = {
            'package_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hairservice': forms.Select(attrs={'class': 'form-control'}),
            'nailservice': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description':  forms.Textarea(attrs={'class': 'form-control'})
        }