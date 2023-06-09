# Generated by Django 4.2.1 on 2023-06-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_subcitymodel_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='headline_news_body',
            field=models.TextField(default='news'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='headline_news_image',
            field=models.ImageField(blank=True, upload_to='media/headline_news'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='headline_news_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='new_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_image',
            field=models.ImageField(blank=True, upload_to='media/news_image/'),
        ),
    ]
