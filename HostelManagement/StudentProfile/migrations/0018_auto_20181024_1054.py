# Generated by Django 2.1 on 2018-10-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0017_auto_20181024_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='ans',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='qno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
