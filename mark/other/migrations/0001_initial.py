# Generated by Django 5.0.6 on 2025-01-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/blog/')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('short_details', models.TextField()),
                ('create', models.DateTimeField(auto_now=True)),
                ('blog_link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twiter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='media/project_images')),
                ('more', models.TextField(blank=True, null=True)),
                ('show_on_home', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/services/')),
                ('heading', models.CharField(max_length=50)),
                ('sub_heading', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('introduction', models.TextField()),
                ('what_is', models.TextField()),
                ('process', models.TextField()),
                ('benefits', models.TextField()),
                ('example', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('details', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media/staff_images/')),
                ('Facebook', models.CharField(max_length=150)),
                ('linkedin', models.CharField(max_length=150)),
                ('mail', models.CharField(max_length=150)),
                ('show_on_home', models.BooleanField(default=True)),
            ],
        ),
    ]
