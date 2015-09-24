# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0071_auto_20150923_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc_rank',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.COCRank'),
        ),
    ]
