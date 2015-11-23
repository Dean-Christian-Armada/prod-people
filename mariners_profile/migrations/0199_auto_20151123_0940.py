# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0198_auto_20151122_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='allotee',
            name='amount',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='allotee',
            name='branch',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
