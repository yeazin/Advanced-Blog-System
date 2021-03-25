# for using django signals post_save
from django.db.models.signals import post_save
# for using django custom user model
from account.models import New_User_Custom
# for using django receiver
from django.dispatch import receiver
# for using models 
from .models import Blog_User

@receiver(post_save, sender=New_User_Custom)
def post_save_blog_user_create(sender,instance,created,**kwargs):
    if created:
        Blog_User.objects.create(user = instance)
