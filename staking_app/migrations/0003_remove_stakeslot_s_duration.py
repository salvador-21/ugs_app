# Generated by Django 5.0.3 on 2024-08-18 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staking_app', '0002_stakelogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakeslot',
            name='s_duration',
        ),
    ]
