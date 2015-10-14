# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0130_auto_20151014_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='marinerstatushistory',
            name='mariner_status_comment',
            field=models.ForeignKey(default=1, to='mariners_profile.MarinerStatusComment'),
        ),
    ]
