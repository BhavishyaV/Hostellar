# Generated by Django 2.1 on 2018-10-22 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0012_auto_20181022_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='student',
        ),
    ]
