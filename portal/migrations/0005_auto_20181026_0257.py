# Generated by Django 2.0.3 on 2018-10-25 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20181026_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 2, 57, 45, 818433)),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 2, 57, 45, 818433)),
        ),
    ]