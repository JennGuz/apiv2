# Generated by Django 3.2.16 on 2023-02-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0061_auto_20230203_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='zip_code',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]