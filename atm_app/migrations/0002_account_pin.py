# Generated by Django 4.2.7 on 2023-12-21 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pin',
            field=models.CharField(default=1234, max_length=4),
            preserve_default=False,
        ),
    ]
