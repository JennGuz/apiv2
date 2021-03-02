# Generated by Django 3.1.6 on 2021-03-02 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0007_bill_academy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='paid_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='bill',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='freelance.bill'),
        ),
    ]
