# Generated by Django 3.2.15 on 2022-10-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '0011_auto_20220825_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetcomment',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assetcomment',
            name='owner',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='In charge of resolving the comment or issue',
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='assigned_comments',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assetcomment',
            name='priority',
            field=models.SmallIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='assetcomment',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assetcomment',
            name='author',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Who wrote the comment or issue',
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]