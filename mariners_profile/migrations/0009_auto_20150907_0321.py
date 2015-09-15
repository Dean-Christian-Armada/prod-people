# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0008_auto_20150906_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip',
            name='zip',
            field=models.PositiveIntegerField(default=None, unique=True),
        ),
    ]
