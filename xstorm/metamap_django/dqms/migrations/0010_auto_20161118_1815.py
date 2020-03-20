# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dqms', '0009_dqmscheck_last_run_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dqmscase',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='case_creator', to='will_common.UserProfile'),
        ),
        migrations.AlterField(
            model_name='dqmscase',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='case_editor', to='will_common.UserProfile'),
        ),
        migrations.AlterField(
            model_name='dqmscheck',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ehk_creator', to='will_common.UserProfile'),
        ),
        migrations.AlterField(
            model_name='dqmscheck',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chk_editor', to='will_common.UserProfile'),
        ),
        migrations.AlterField(
            model_name='dqmscheck',
            name='last_run_time',
            field=models.DateTimeField(),
        ),
    ]
