# Generated by Django 5.0.3 on 2024-08-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0039_alter_uwalletcashout_cw_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uwalletcashout',
            name='cw_agent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
