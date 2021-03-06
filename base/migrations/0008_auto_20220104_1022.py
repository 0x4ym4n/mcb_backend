# Generated by Django 3.1.7 on 2022-01-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20220104_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='office',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_office', to='base.office'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='seats',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
