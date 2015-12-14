# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0212_auto_20151209_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
