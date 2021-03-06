# Generated by Django 3.2.3 on 2021-12-19 09:29

from django.db import migrations, models
import django.db.models.deletion
import thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('activity', models.CharField(blank=True, max_length=250)),
                ('business_type', models.CharField(blank=True, default='Limited by Shares', max_length=250)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('company_type', models.IntegerField(blank=True, default=0)),
                ('shares', models.IntegerField(blank=True, default=0)),
                ('rental', models.FileField(blank=True, upload_to='static/uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('seat_price', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_type', models.IntegerField(blank=True, default=0)),
                ('reference_id', models.IntegerField(blank=True, default=0)),
                ('director', models.BooleanField(default=False)),
                ('shares', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('birthday', models.CharField(blank=True, max_length=250)),
                ('nationality', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('photo', thumbnails.fields.ImageField(blank=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('photo', thumbnails.fields.ImageField(blank=True, upload_to='static/images')),
                ('company_certificate', models.FileField(blank=True, upload_to='static/uploads')),
                ('moa', models.FileField(blank=True, upload_to='static/uploads')),
                ('signatory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signing_person', to='base.person')),
            ],
        ),
    ]
