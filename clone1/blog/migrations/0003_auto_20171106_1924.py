# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171106_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 19, 24, 53, 31718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 19, 24, 53, 30979, tzinfo=utc)),
        ),
    ]
