# Inside your app's forms.py file
from django import forms
from .models import User
class RegisterForm(forms.ModelForm):
  class Meta:
      model = User
      fields = '__all__'