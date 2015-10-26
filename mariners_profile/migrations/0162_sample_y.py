# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0161_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='y',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
