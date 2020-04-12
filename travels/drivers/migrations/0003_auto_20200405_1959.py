# Generated by Django 3.0.4 on 2020-04-05 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20200405_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='commercial_badge',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='driving_license',
        ),
        migrations.AddField(
            model_name='driver',
            name='badge_expiry',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='license_expiry',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]