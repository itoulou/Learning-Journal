# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_resource_test', '0004_auto_20190918_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='database',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='framework',
            name='framework',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='technology',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
