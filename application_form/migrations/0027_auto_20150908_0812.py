# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0026_auto_20150908_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformlicense',
            name='license_rank',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.Rank'),
        ),
        migrations.AlterField(
            model_name='applicationformschengenvisa',
            name='schengen_visa',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='applicationformusvisa',
            name='us_visa',
            field=models.NullBooleanField(),
        ),
    ]
