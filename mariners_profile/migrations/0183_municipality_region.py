# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0182_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='region',
            field=models.ForeignKey(default=19, to='mariners_profile.Region'),
        ),
    ]
