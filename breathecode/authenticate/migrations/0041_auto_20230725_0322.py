# Generated by Django 3.2.19 on 2023-07-25 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0040_userinvite_is_email_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='user',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='invites',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='author',
            field=models.ForeignKey(default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='invites_by_author',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
