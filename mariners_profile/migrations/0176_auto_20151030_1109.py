# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0175_auto_20151030_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marinerstatushistory',
            name='mariner_principal',
            field=models.ForeignKey(default=8, to='mariners_profile.Principal'),
        ),
    ]
