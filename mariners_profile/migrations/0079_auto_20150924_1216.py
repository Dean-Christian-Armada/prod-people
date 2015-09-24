# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0078_auto_20150924_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='evalutation',
            new_name='evaluation',
        ),
    ]
