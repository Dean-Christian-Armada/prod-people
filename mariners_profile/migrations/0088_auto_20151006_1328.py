# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0087_principalvesseltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchengenVisaPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schengen_visa_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='USVisaPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_visa_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YellowFeverPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yellow_fever_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='passportplaceissued',
            old_name='place',
            new_name='passport_place',
        ),
        migrations.RenameField(
            model_name='sbookplaceissued',
            old_name='place',
            new_name='sbook_place',
        ),
    ]
