# Generated by Django 3.1.5 on 2021-03-17 08:34

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True, verbose_name='Topics')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Topics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='BlogPart.topics')),
            ],
        ),
    ]
