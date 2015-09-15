# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0049_auto_20150911_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaservice',
            name='duration',
            field=models.PositiveSmallIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='grt',
            field=models.PositiveIntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.DecimalField(default=None, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.DecimalField(default=None, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='year_built',
            field=models.PositiveSmallIntegerField(default=None, blank=True),
        ),
    ]
