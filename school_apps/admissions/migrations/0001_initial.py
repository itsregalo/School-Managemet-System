# Generated by Django 3.2.3 on 2021-11-01 17:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_auto_20211013_1941'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('other_name', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('mobile_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')])),
                ('address', models.TextField(blank=True)),
                ('others', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Madam', 'Madam')], max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('teacher_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('Bi', 'Bisexual'), ('Other', 'Other')], max_length=100)),
                ('adm_timestamp', models.DateTimeField(auto_now_add=True)),
                ('has_cleared', models.BooleanField(default=False)),
                ('in_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.studentclass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('adress', models.TextField()),
                ('students', models.ManyToManyField(to='admissions.Student')),
            ],
        ),
    ]
