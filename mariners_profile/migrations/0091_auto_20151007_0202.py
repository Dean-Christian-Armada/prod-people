# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0090_auto_20151007_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='coc_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.COCPlaceIssued'),
        ),
        migrations.AddField(
            model_name='license',
            name='license_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.LicensePlaceIssued'),
        ),
    ]
