# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0043_auto_20150922_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformcoc',
            name='coc_rank',
            field=models.ForeignKey(default=None, blank=True, to='mariners_profile.COCRank'),
        ),
    ]
