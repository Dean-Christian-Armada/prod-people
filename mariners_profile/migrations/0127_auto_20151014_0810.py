# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0126_auto_20151014_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinersprofile',
            name='mariner_status',
            field=models.ForeignKey(default=1, to='mariners_profile.MarinerStatus'),
        ),
        migrations.AddField(
            model_name='marinerstatushistory',
            name='mariner_status',
            field=models.ForeignKey(default=1, to='mariners_profile.MarinerStatus'),
        ),
    ]
