# Generated by Django 2.1 on 2018-10-19 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0006_auto_20181019_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetails',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='StudentProfile.Profile'),
        ),
    ]
