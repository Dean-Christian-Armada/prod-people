# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0203_remove_marinerstatushistory_mariner_status_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=38, to='mariners_profile.Principal'),
        ),
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_status',
            field=models.ForeignKey(default=None, to='mariners_profile.MarinerStatus'),
        ),
    ]
