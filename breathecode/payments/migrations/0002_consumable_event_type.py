# Generated by Django 3.2.16 on 2022-12-08 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0033_auto_20221208_1246'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumable',
            name='event_type',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='events.eventtype'),
        ),
    ]
