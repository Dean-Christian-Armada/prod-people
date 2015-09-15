# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0009_auto_20150907_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentaddress',
            old_name='street',
            new_name='current_street',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='unit',
            new_name='current_unit',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='zip',
            new_name='current_zip',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='street',
            new_name='permanent_street',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='unit',
            new_name='permanent_unit',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='zip',
            new_name='permanent_zip',
        ),
    ]
