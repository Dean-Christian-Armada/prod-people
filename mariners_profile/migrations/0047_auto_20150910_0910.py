# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0046_rank_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifics',
            name='specific',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
    ]
