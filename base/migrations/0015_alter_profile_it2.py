# Generated by Django 4.0.3 on 2022-04-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_profile_face_tmp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='it2',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
