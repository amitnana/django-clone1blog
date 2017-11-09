# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171106_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 20, 6, 40, 980652, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 20, 6, 40, 979898, tzinfo=utc)),
        ),
    ]