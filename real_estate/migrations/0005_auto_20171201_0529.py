# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-01 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0004_bhgeometry_searchhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhistory',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
