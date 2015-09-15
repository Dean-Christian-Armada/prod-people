# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0045_rank_hiring'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='order',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
    ]
