# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0070_remove_vocationals_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocrank',
            name='coc_rank',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
