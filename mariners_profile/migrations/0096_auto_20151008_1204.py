# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0095_seaservice_trade_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinersprofile',
            name='date_hired',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='trade_area',
            field=models.ForeignKey(to='mariners_profile.TradeArea'),
        ),
    ]
