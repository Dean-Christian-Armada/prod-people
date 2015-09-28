# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0079_auto_20150924_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='financial_liability',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reference',
            name='rehiring_prospects',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reference',
            name='veracity_seagoing_history',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
