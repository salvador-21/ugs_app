# Generated by Django 5.0.3 on 2024-08-15 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0021_userwallet_w_betlong_userwallet_w_betwins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='w_betlong',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='w_betwins',
        ),
    ]
