# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-07 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamap', '0017_auto_20161207_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqoophive2mysql',
            name='settings',
            field=models.TextField(null=True),
        ),
    ]
