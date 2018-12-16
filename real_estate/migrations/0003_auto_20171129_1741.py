# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-29 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0002_auto_20171107_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertydetail',
            name='open_house_upcoming',
        ),
        migrations.AddField(
            model_name='property',
            name='open_house_upcoming',
            field=models.CharField(max_length=200, null=True),
        ),
    ]