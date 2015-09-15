# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150906_0634'),
        ('mariners_profile', '0041_auto_20150909_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeaService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grt', models.PositiveIntegerField(default=None)),
                ('dwt', models.PositiveIntegerField(default=None)),
                ('year_built', models.PositiveSmallIntegerField(default=None)),
                ('duration', models.PositiveSmallIntegerField(default=None)),
                ('hp', models.DecimalField(default=None, max_digits=10, decimal_places=1)),
                ('kw', models.DecimalField(default=None, max_digits=10, decimal_places=1)),
                ('date_joined', models.DateField(default=None)),
                ('date_left', models.DateField(default=None)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('cause_of_discharge', models.ForeignKey(default=None, to='mariners_profile.CauseOfDischarge')),
                ('engine_type', models.ForeignKey(default=None, to='mariners_profile.EngineType')),
                ('flag', models.ForeignKey(default=None, to='mariners_profile.Flags')),
                ('manning_agency', models.ForeignKey(default=None, to='mariners_profile.ManningAgency')),
                ('principal', models.ForeignKey(default=None, to='mariners_profile.Principal')),
                ('rank', models.ForeignKey(default=None, to='mariners_profile.Rank')),
                ('user', models.ForeignKey(default=None, to='login.UserProfile')),
                ('vessel_name', models.ForeignKey(default=None, to='mariners_profile.VesselName')),
                ('vessel_type', models.ForeignKey(default=None, to='mariners_profile.VesselType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
