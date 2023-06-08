# Generated by Django 4.2.1 on 2023-06-07 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinete_name', models.CharField(max_length=255)),
                ('education_preparation', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('cabinete_image', models.ImageField(upload_to='media/cabinetes/')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('cabinete_title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_person_name', models.CharField(max_length=255)),
                ('comment_sector', models.CharField(max_length=255)),
                ('comment_body', models.TextField()),
                ('date_commented', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_commented',),
            },
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.TextField()),
                ('event_image', models.ImageField(upload_to='media/event_image/')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='media/gallery/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=255)),
                ('office_image', models.ImageField(upload_to='media/offices/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_executive_name', models.CharField(max_length=200)),
                ('chief_executive_image', models.ImageField(upload_to='media/chief_executive/')),
                ('chief_executive_message', models.TextField(blank=True)),
                ('carousel_image', models.ImageField(blank=True, upload_to='media/carousels/')),
                ('carousel_title', models.TextField()),
                ('area_of_subcity', models.IntegerField()),
                ('population', models.IntegerField()),
                ('elivation', models.IntegerField()),
                ('fax', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('pobox', models.CharField(blank=True, max_length=20)),
                ('facebook_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_title', models.CharField(max_length=255)),
                ('tender_description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('expired_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_title', models.CharField(max_length=255)),
                ('vacancy_description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('expired_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WoredaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woreda_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fax', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('pobox', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_title', models.CharField(max_length=255)),
                ('news_body', models.TextField()),
                ('news_image', models.ImageField(upload_to='media/news_image/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
