# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0176_auto_20151030_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=None, to='mariners_profile.Principal'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_status',
            field=models.ForeignKey(default=8, to='mariners_profile.MarinerStatus'),
        ),
    ]
