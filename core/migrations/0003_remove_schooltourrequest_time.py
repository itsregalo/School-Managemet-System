# Generated by Django 3.2.3 on 2021-10-10 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_schooltourrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooltourrequest',
            name='time',
        ),
    ]