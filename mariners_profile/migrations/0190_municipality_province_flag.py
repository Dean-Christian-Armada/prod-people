# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0189_auto_20151109_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='province_flag',
            field=models.BooleanField(default=True),
        ),
    ]
