# Generated by Django 2.1 on 2018-10-22 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0014_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetails',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudentProfile.Profile'),
        ),
    ]
