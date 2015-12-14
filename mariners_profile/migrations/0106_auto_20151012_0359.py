# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0105_trainingcertificatedocumentsdetailed_expiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='STCWEndorsement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stcw_endorsement', models.CharField(default=None, unique=True, max_length=100)),
                ('stcw_endorsement_date_issued', models.DateField(default=None, null=True, blank=True)),
                ('stcw_endorsement_date_expiry', models.DateField(default=None, null=True, blank=True)),
                ('stcw_endorsement_rank', models.ForeignKey(default={'rank': ''}, to='mariners_profile.Rank')),
            ],
        ),
        migrations.RenameField(
            model_name='license',
            old_name='license_expiry',
            new_name='license_date_expiry',
        ),
        migrations.RenameField(
            model_name='src',
            old_name='src_expiry',
            new_name='src_date_expiry',
        ),
        migrations.AddField(
            model_name='passport',
            name='passport_date_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sbook',
            name='sbook_date_expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
