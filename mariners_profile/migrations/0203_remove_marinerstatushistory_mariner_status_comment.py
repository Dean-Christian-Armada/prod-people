# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0202_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marinerstatushistory',
            name='mariner_status_comment',
        ),
    ]
