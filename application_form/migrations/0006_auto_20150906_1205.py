# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0005_auto_20150906_1205'),
        ('application_form', '0005_auto_20150906_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='birth_place',
            field=models.ForeignKey(default=None, to='mariners_profile.BirthPlace'),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='civil_status',
            field=models.ForeignKey(default=None, to='mariners_profile.CivilStatus'),
        ),
        migrations.AddField(
            model_name='applicationformpersonaldata',
            name='preferred_vessel_type',
            field=models.ForeignKey(default=None, to='mariners_profile.VesselType'),
        ),
    ]
