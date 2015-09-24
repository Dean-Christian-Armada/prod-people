# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0072_auto_20150923_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='goc',
            name='goc',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
