# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0183_municipality_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='region',
            field=models.ForeignKey(default=20, to='mariners_profile.Region'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='zip',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
