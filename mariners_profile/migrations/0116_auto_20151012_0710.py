# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0115_auto_20151012_0622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schengenvisa',
            name='schengen_visa_date_expiry',
        ),
        migrations.RemoveField(
            model_name='usvisa',
            name='us_visa_date_expiry',
        ),
    ]
