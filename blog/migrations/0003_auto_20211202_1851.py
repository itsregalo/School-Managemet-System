# Generated by Django 3.2.3 on 2021-12-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_is_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_date'], 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name': 'blog comment', 'verbose_name_plural': 'blog comments'},
        ),
        migrations.AlterModelOptions(
            name='blogtags',
            options={'verbose_name': 'blog tag', 'verbose_name_plural': 'blog tags'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]