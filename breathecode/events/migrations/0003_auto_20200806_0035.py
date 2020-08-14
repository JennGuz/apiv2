# Generated by Django 3.0.8 on 2020-08-06 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0008_auto_20200708_0049'),
        ('events', '0002_auto_20200806_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='academy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.Academy'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='academy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.Academy'),
        ),
        migrations.AddField(
            model_name='venue',
            name='academy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.Academy'),
        ),
    ]