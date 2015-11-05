# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20151105_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='subfolder',
            name='upload',
            field=models.BooleanField(default=True),
        ),
    ]
