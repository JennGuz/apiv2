# Generated by Django 3.2 on 2021-05-22 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0018_alter_cohortuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CohortTimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_at', models.DateTimeField()),
                ('ending_at', models.DateTimeField()),
                ('recurrent', models.BooleanField(default=True)),
                ('recurrency_type', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], default='WEEKLY', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.cohort')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CertificateTimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_at', models.DateTimeField()),
                ('ending_at', models.DateTimeField()),
                ('recurrent', models.BooleanField(default=True)),
                ('recurrency_type', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], default='WEEKLY', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.academy')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.certificate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]