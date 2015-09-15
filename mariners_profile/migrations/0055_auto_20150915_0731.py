# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0054_auto_20150915_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
    ]
