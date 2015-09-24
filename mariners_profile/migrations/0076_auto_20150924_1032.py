# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0075_auto_20150924_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
