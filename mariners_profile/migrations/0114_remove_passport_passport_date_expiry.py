# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0113_auto_20151012_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passport',
            name='passport_date_expiry',
        ),
    ]
