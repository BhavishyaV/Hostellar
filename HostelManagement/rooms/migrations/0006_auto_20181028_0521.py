# Generated by Django 2.1 on 2018-10-28 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20181028_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='occupation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]