# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-28 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamap', '0029_auto_20170228_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceapp',
            name='engine_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='metamap.SourceEngine', verbose_name='\u8fd0\u884c\u5de5\u5177 \uff1a java,spakr,hadoop\u7b49'),
        ),
    ]
