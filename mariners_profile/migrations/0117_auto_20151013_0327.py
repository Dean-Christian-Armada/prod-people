# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0116_auto_20151012_0710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allotee',
            old_name='relationship',
            new_name='allotee_relationship',
        ),
    ]
