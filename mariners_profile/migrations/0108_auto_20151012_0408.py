# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0107_auto_20151012_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stcwendorsement',
            name='stcw_endorsement_rank',
            field=models.ForeignKey(default={b'rank': b'asdasdas'}, to='mariners_profile.Rank'),
        ),
    ]
