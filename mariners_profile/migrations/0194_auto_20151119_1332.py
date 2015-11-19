# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0193_auto_20151119_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='municipality',
            field=models.CharField(default=None, unique=True, max_length=50),
        ),
    ]
