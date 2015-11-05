# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20151105_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfolder',
            name='extra_sub_folder',
            field=models.ForeignKey(default=None, to='cms.SubFolder'),
        ),
        migrations.AlterField(
            model_name='subfolder',
            name='folder',
            field=models.ForeignKey(default=7, to='cms.Folder'),
        ),
    ]
