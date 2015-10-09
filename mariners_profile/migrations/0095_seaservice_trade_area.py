# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0094_tradearea'),
    ]

    operations = [
        migrations.AddField(
            model_name='seaservice',
            name='trade_area',
            field=models.ForeignKey(default=1, to='mariners_profile.TradeArea'),
        ),
    ]
