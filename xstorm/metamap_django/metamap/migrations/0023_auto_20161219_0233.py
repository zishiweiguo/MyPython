# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-19 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamap', '0022_sqoopmysql2hive_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqoopmysql2hive',
            name='partition_key',
            field=models.CharField(default=b'', max_length=300, null=True),
        ),
    ]
