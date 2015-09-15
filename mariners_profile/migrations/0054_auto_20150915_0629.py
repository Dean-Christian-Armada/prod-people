# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0053_auto_20150914_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='grt',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
