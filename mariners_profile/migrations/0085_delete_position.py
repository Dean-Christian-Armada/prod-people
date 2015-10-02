# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0084_auto_20151001_1057'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Position',
        ),
    ]
