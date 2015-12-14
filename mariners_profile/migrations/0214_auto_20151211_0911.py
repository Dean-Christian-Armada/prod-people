# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0213_auto_20151211_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotee',
            name='amount',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True),
        ),
    ]
