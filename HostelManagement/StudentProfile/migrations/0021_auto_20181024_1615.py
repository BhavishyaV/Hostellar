# Generated by Django 2.1 on 2018-10-24 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0020_auto_20181024_1506'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quiz',
            unique_together={('profile', 'qno')},
        ),
    ]
