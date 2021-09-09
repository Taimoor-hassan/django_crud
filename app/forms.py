from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import student

class entryform (forms.ModelForm):
 class Meta:
       model = student
       fields = ['name', 'email']
       widgets={
           'name': forms.TextInput(),
           'email': forms.EmailInput(),
       }