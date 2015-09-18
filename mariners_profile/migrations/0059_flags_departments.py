# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0058_auto_20150918_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='flags',
            name='departments',
            field=models.ManyToManyField(default=6, to='mariners_profile.Departments'),
        ),
    ]
