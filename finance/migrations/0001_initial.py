# Generated by Django 3.2.3 on 2021-10-09 15:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admissions', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_from_previous_term', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=20)),
                ('class_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.studentclass')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academicsession')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academicterm')),
            ],
            options={
                'ordering': ['student', 'term'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField()),
                ('date_paid', models.DateField(default=django.utils.timezone.now)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.invoice')),
            ],
        ),
    ]
