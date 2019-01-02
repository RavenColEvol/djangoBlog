from django import forms
from django.contrib.auth.models import User
from .models import BlogPosts,BlogUser
class BlogForms(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields= '__all__'

class UserName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')