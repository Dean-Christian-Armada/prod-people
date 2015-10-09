# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0091_auto_20151007_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coc',
            name='coc_number',
        ),
        migrations.RemoveField(
            model_name='license',
            name='license_number',
        ),
    ]
