# Generated by Django 3.1.5 on 2021-03-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPart', '0006_remove_blog_user_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='username',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog_user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
