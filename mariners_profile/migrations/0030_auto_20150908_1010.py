# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0029_auto_20150908_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goc',
            name='goc_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='src',
            name='src_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='src',
            name='src_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
