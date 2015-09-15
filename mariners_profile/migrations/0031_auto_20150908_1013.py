# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0030_auto_20150908_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schengenvisa',
            name='schengen_visa_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='us_visa_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
