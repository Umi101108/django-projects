# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(default=datetime.datetime(2016, 12, 15, 7, 32, 31, 209000, tzinfo=utc), max_length=11),
            preserve_default=False,
        ),
    ]
