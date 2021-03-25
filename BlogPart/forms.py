from django.forms import forms,ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  Blog_Post

class Create_Post_Forms(ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['title','body','Topics','feature_image']


