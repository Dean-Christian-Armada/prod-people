# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0121_auto_20151013_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='relationship',
            new_name='beneficiary_relationship',
        ),
    ]
