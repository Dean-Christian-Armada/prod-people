# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0173_auto_20151030_0648'),
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
            field=models.ForeignKey(default=None, to='mariners_profile.MarinerStatus'),
        ),
    ]
