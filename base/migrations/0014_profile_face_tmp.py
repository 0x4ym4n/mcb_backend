# Generated by Django 4.0.3 on 2022-04-01 13:36

from django.db import migrations
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_profile_face_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='face_tmp',
            field=thumbnails.fields.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
