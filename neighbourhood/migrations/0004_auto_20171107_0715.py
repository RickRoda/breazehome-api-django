# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-07 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20171107_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazard',
            name='DATA_SOURCE',
            field=models.CharField(max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hazard',
            name='EPISODE_NARRATIVE',
            field=models.CharField(max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hazard',
            name='EVENT_NARRATIVE',
            field=models.CharField(max_length=50000, null=True),
        ),
    ]
