# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0207_auto_20151202_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='src',
            name='src_rank',
            field=models.ForeignKey(to='mariners_profile.Rank', default="mariners_profile.null_default_foreign_key_value(Rank, 'rank', '')"),
        ),
    ]
