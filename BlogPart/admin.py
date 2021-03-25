from django.contrib import admin
from .models import Topics,Blog_Post, Upvote, Downvote, Blog_User

# Register your models here.

admin.site.register(Topics)
admin.site.register(Blog_Post)
admin.site.register(Blog_User)
admin.site.register(Upvote)
admin.site.register(Downvote)