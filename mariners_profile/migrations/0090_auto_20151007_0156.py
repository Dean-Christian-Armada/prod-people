# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0089_auto_20151006_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='COCPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LicensePlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='coc',
            name='coc_grade',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coc',
            name='coc_number',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='license',
            name='license_grade',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='license',
            name='license_number',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schengenvisa',
            name='schengen_visa_place_issued',
            field=models.ForeignKey(to='mariners_profile.SchengenVisaPlaceIssued', blank=True),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='us_visa_place_issued',
            field=models.ForeignKey(to='mariners_profile.USVisaPlaceIssued', blank=True),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='yellow_fever_place_issued',
            field=models.ForeignKey(to='mariners_profile.YellowFeverPlaceIssued', blank=True),
        ),
    ]
