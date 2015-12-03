# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0204_auto_20151202_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_status',
            field=models.ForeignKey(default=2, to='mariners_profile.MarinerStatus'),
        ),
    ]
