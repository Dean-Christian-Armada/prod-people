# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0141_issuingauthority'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='coc_issuing_authority',
            field=models.ForeignKey(default=1, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AddField(
            model_name='ntclicense',
            name='passport_issuing_authority',
            field=models.ForeignKey(default=1, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AddField(
            model_name='passport',
            name='passport_issuing_authority',
            field=models.ForeignKey(default=1, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AddField(
            model_name='sbook',
            name='sbook_issuing_authority',
            field=models.ForeignKey(default=1, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AlterField(
            model_name='coc',
            name='coc_place_issued',
            field=models.ForeignKey(default=4, blank=True, to='mariners_profile.COCPlaceIssued'),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_place_issued',
            field=models.ForeignKey(default=4, blank=True, to='mariners_profile.LicensePlaceIssued'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='passport_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.PassportPlaceIssued'),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='sbook_place_issued',
            field=models.ForeignKey(default=1, blank=True, to='mariners_profile.SBookPlaceIssued'),
        ),
    ]
