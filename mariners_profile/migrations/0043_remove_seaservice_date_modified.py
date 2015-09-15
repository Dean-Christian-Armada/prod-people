# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0042_seaservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seaservice',
            name='date_modified',
        ),
    ]
