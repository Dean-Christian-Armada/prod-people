# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0145_auto_20151019_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='coc_issuing_authority',
            field=models.ForeignKey(default=2, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AddField(
            model_name='passport',
            name='passport_issuing_authority',
            field=models.ForeignKey(default=3, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AddField(
            model_name='sbook',
            name='sbook_issuing_authority',
            field=models.ForeignKey(default=2, to='mariners_profile.IssuingAuthority'),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='yellow_fever_issuing_authority',
            field=models.ForeignKey(default=4, to='mariners_profile.IssuingAuthority'),
        ),
    ]
