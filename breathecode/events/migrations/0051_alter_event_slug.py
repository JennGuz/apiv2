# Generated by Django 3.2.19 on 2023-07-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0050_auto_20230721_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=150, null=True, unique=True),
        ),
    ]
