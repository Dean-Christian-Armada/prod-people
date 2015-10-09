# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0100_beneficiary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landemployment',
            old_name='position',
            new_name='land_position',
        ),
    ]
