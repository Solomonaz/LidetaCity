# Generated by Django 4.2.1 on 2023-06-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_gallerymodel_options_gallerymodel_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerymodel',
            name='gallery_title',
            field=models.CharField(default='some title', max_length=100),
            preserve_default=False,
        ),
    ]
