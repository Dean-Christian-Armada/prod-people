# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0199_auto_20151123_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.DecimalField(default=None, null=True, max_digits=10, decimal_places=1, blank=True),
        ),
    ]
