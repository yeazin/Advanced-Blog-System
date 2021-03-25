from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from BlogPart.models import Blog_User
from .models import New_User_Custom

class BlogUser_Forms(UserCreationForm):
    class Meta:
        model = New_User_Custom
        fields = ['user_name','first_name','email', 'password1','password2']