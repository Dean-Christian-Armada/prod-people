# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0027_auto_20150908_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_rank',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Rank'),
        ),
        migrations.AlterField(
            model_name='schengenvisa',
            name='schengen_visa',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='us_visa',
            field=models.NullBooleanField(),
        ),
    ]
