# Generated by Django 3.1.7 on 2022-01-05 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_company_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_office', to='base.office'),
        ),
    ]
