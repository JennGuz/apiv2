# Generated by Django 3.1.4 on 2020-12-18 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0014_auto_20201218_0534'),
        ('marketing', '0027_shortlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='academy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admissions.academy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formentry',
            name='academy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.academy'),
        ),
        migrations.CreateModel(
            name='ActiveCampaignAcademy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_key', models.CharField(max_length=150)),
                ('ac_url', models.CharField(max_length=150)),
                ('sync_status', models.CharField(choices=[('INCOMPLETED', 'Incompleted'), ('COMPLETED', 'Completed')], default='INCOMPLETED', help_text='Automatically set when interacting with the Active Campaign API', max_length=15)),
                ('sync_message', models.CharField(blank=True, default=None, help_text='Contains any success or error messages depending on the status', max_length=100, null=True)),
                ('last_interaction_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admissions.academy')),
            ],
        ),
        migrations.AddField(
            model_name='automation',
            name='ac_academy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketing.activecampaignacademy'),
        ),
        migrations.AddField(
            model_name='formentry',
            name='ac_academy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketing.activecampaignacademy'),
        ),
        migrations.AddField(
            model_name='tag',
            name='ac_academy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketing.activecampaignacademy'),
        ),
    ]
