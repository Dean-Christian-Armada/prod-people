# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0178_auto_20151030_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=35, to='mariners_profile.Principal'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_status',
            field=models.ForeignKey(default=9, to='mariners_profile.MarinerStatus'),
        ),
    ]
