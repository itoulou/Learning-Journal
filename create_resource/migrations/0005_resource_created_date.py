# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-10 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create_resource', '0004_auto_20190910_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 10, 12, 28, 36, 893816, tzinfo=utc), null=True),
        ),
    ]