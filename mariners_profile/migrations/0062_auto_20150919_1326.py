# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0061_auto_20150918_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='department',
            field=models.ForeignKey(default=5, to='mariners_profile.Departments'),
        ),
    ]
