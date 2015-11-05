# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_subfolder_extra_sub_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfolder',
            name='extra_sub_folder',
            field=models.ForeignKey(default=9, to='cms.SubFolder'),
        ),
    ]
