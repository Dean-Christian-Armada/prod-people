# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0110_auto_20151012_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='NTCLicense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ntc_license', models.CharField(default=None, unique=True, max_length=100)),
                ('ntc_license_date_issued', models.DateField(default=None, null=True, blank=True)),
                ('ntc_license_date_expiry', models.DateField(default=None, null=True, blank=True)),
                ('ntc_license_rank', models.ForeignKey(default=22, to='mariners_profile.Rank')),
            ],
        ),
        migrations.CreateModel(
            name='STCWCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stcw_certificate', models.CharField(default=None, unique=True, max_length=100)),
                ('stcw_certificate_date_issued', models.DateField(default=None, null=True, blank=True)),
                ('stcw_certificate_date_expiry', models.DateField(default=None, null=True, blank=True)),
                ('stcw_certificate_rank', models.ForeignKey(default=22, to='mariners_profile.Rank')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlaceIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training_place', models.CharField(default=None, max_length=50, blank=True)),
                ('company_standard', models.NullBooleanField(default=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags_rank',
            field=models.ForeignKey(default=22, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='goc',
            name='goc_rank',
            field=models.ForeignKey(default=22, to='mariners_profile.Rank'),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='schengen_visa_date_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='schengenvisa',
            name='schengen_visa_number',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='us_visa_date_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usvisa',
            name='us_visa_number',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='place_trained',
            field=models.ForeignKey(default=1, to='mariners_profile.TrainingCenter'),
        ),
    ]
