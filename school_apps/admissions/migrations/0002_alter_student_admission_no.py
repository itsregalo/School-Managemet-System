# Generated by Django 3.2.3 on 2021-10-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]