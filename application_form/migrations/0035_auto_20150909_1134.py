# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0042_seaservice'),
        ('login', '0007_auto_20150906_0634'),
        ('application_form', '0034_applicationformabstractseaservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormSeaService',
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
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='cause_of_discharge',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='manning_agency',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='principal',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='user',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='vessel_name',
        ),
        migrations.RemoveField(
            model_name='applicationformabstractseaservice',
            name='vessel_type',
        ),
        migrations.DeleteModel(
            name='ApplicationFormAbstractSeaService',
        ),
    ]
