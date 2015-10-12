# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0109_auto_20151012_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stcwendorsement',
            name='stcw_endorsement_rank',
            field=models.ForeignKey(default=22, to='mariners_profile.Rank'),
        ),
    ]
