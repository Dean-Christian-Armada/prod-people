# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0192_auto_20151112_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangay',
            name='barangay',
            field=models.CharField(default=None, unique=True, max_length=50),
        ),
    ]
