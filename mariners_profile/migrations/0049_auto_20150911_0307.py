# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0048_auto_20150910_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marinersprofile',
            old_name='signatures',
            new_name='signature',
        ),
    ]
