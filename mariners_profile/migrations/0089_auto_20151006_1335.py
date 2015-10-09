# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0088_auto_20151006_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='schengenvisa',
            name='schengen_visa_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='schengen_visa_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.SchengenVisaPlaceIssued'),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='us_visa_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='us_visa_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.USVisaPlaceIssued'),
        ),
        migrations.AddField(
            model_name='yellowfever',
            name='yellow_fever_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='yellowfever',
            name='yellow_fever_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.YellowFeverPlaceIssued'),
        ),
    ]
