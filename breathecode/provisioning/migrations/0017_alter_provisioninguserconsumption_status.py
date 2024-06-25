# Generated by Django 5.0.6 on 2024-06-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provisioning', '0016_alter_provisioningconsumptionevent_repository_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provisioninguserconsumption',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PERSISTED', 'Persisted'), ('IGNORED', 'Ignored'),
                                            ('WARNING', 'Warning'), ('ERROR', 'Error')],
                                   default='PENDING',
                                   max_length=20),
        ),
    ]
