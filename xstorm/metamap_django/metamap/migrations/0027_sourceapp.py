# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-27 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('will_common', '0002_auto_20161219_0819'),
        ('auth', '0007_alter_validators_add_error_messages'),
        ('metamap', '0026_auto_20161219_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('git_url', models.CharField(max_length=200, verbose_name='git\u5730\u5740')),
                ('sub_dir', models.CharField(max_length=100, verbose_name='\u5de5\u4f5c\u76ee\u5f55')),
                ('branch', models.CharField(max_length=20, verbose_name='git\u5206\u652f')),
                ('compile_tool', models.CharField(max_length=20, verbose_name='\u7f16\u8bd1\u5de5\u5177 \uff1a maven, ant\u7b49')),
                ('engine_type', models.CharField(max_length=20, verbose_name='\u8fd0\u884c\u5de5\u5177 \uff1a java,spakr,hadoop\u7b49')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.IntegerField(blank=True, default=5)),
                ('valid', models.IntegerField(default=1, verbose_name='\u662f\u5426\u751f\u6548')),
                ('setting', models.CharField(default=b'', max_length=200, verbose_name='\u8fd0\u884c\u53c2\u6570')),
                ('cgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='source_cgroup', to='auth.Group')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='source_creator', to='will_common.UserProfile')),
            ],
        ),
    ]
