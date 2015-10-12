# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0106_auto_20151012_0359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='license_date_expiry',
            new_name='license_expiry',
        ),
        migrations.RenameField(
            model_name='src',
            old_name='src_date_expiry',
            new_name='src_expiry',
        ),
    ]
