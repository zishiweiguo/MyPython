# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-07 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamap', '0015_sqoophive2mysql_partion_expr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqoophive2mysql',
            name='partion_expr',
            field=models.TextField(null=True),
        ),
    ]