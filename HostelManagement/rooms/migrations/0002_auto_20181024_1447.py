# Generated by Django 2.1 on 2018-10-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('block', 'room_no')},
        ),
    ]
