# Generated by Django 3.2.3 on 2021-12-01 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211130_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicsession',
            options={'ordering': ['-name'], 'verbose_name': 'Academic Session', 'verbose_name_plural': 'Academic Sessions'},
        ),
        migrations.AlterModelOptions(
            name='academicterm',
            options={'ordering': ['-name'], 'verbose_name': 'Academic Term', 'verbose_name_plural': 'Academic Terms'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
