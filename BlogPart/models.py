from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from account.models import New_User_Custom
from django.conf import settings
from AdvancedBlog.settings import AUTH_USER_MODEL



#topics Model
class Topics(models.Model):
    name = models.CharField(max_length=200,null= True,blank=False, unique=True, verbose_name='Topics')
    slug = AutoSlugField(populate_from='name') 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='Topics'

# Upvotes class
class Upvote(models.Model):
    user    =   models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    votes   =   models.IntegerField(blank=True, editable=False, null=True)

    def __str__(self):
        return self.votes.user_upvote

    class Meta:
        verbose_name='Upvote'
        verbose_name_plural ='Upvotes'

# Downvotes class

class Downvote(models.Model):
    user    =   models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    votes   =   models.IntegerField( blank=True, editable=False, null=True)

    def __str__(self):
        return self.votes.user_downvote

    class Meta:
        verbose_name ='Downvote'
        verbose_name_plural = 'Downvotes'


class Blog_Post(models.Model):

    user            =   models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_post', null=True)
    title           =   models.CharField(max_length=300, blank=False, editable=True)
    body            =   RichTextField(blank=True, null=True)
    Topics          =   models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='topics')
    feature_image   =   models.FileField(upload_to='media/post',blank=False, null=True)
    created         =   models.DateTimeField(auto_now_add=True,null=True)
    updated         =   models.DateTimeField(auto_now=True)
    


    def short(self):
        shortbody = body[:10]
        return shortbody
        
    def __str__(self):
        return self.title

        


#User information 

class Blog_User(models.Model):
    user        =   models.OneToOneField(New_User_Custom, on_delete=models.CASCADE)
    user_name    =   models.CharField(max_length=200, unique=True, blank=False,null=True)
    bio         =   models.TextField(blank=True)
    first_name  =   models.CharField(blank=False, max_length=100,null=True)
    last_name   =   models.CharField(blank=True, max_length=100,null=True)
    email       =   models.EmailField(unique=True, blank=False, null=True)
    created     =   models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.first_name
