# Generated by Django 4.2.1 on 2023-06-07 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_newsmodel_headline_news_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadlineNewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_news_title', models.CharField(blank=True, max_length=255)),
                ('headline_news_body', models.TextField()),
                ('headline_news_image', models.ImageField(blank=True, upload_to='media/headline_news')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
