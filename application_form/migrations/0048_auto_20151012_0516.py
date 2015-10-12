# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0047_auto_20151002_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformsrc',
            name='src_rank',
            field=models.ForeignKey(default=b"mariners_profile.null_default_foreign_key_value(Rank, 'rank', '')", to='mariners_profile.Rank'),
        ),
    ]
