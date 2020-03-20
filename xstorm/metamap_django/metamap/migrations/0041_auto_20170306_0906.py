# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-06 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metamap', '0040_jarapp_jar_file'),
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='ETLBlood',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('ctime', models.DateTimeField(default=django.utils.timezone.now)),
    #         ],
    #     ),
    #     migrations.CreateModel(
    #         name='ExecObj',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('name', models.CharField(db_column=b'name', max_length=100)),
    #             ('type', models.IntegerField(default=1, help_text=b'1 ETL; 2 EMAIL; 3 Hive2Mysql; 4 Mysql2Hive; 5 sourcefile;6 jarfile')),
    #             ('rel_id', models.IntegerField()),
    #         ],
    #     ),
    #     migrations.RenameField(
    #         model_name='etl',
    #         old_name='tblName',
    #         new_name='name',
    #     ),
    #     migrations.AlterField(
    #         model_name='jarapp',
    #         name='jar_file',
    #         field=models.FileField(blank=True, upload_to=b'jars'),
    #     ),
    #     migrations.AddField(
    #         model_name='etlblood',
    #         name='child',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='metamap.ExecObj'),
    #     ),
    #     migrations.AddField(
    #         model_name='etlblood',
    #         name='parent',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent', to='metamap.ExecObj'),
    #     ),
    # ]
