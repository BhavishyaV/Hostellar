# Generated by Django 2.1 on 2018-10-19 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfile', '0003_auto_20181019_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade12', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='StudentProfile.Profile')),
            ],
        ),
    ]
