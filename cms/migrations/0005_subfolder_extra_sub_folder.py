# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20151105_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='subfolder',
            name='extra_sub_folder',
            field=models.ForeignKey(default=5, to='cms.SubFolder'),
        ),
    ]
