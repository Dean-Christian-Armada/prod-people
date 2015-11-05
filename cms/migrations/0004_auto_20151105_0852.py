# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20151105_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfolder',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
