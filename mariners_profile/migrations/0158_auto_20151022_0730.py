# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0157_auto_20151022_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coc',
            name='coc_issuing_authority',
            field=models.ForeignKey(default=2, blank=True, to='mariners_profile.IssuingAuthority', null=True),
        ),
        migrations.AlterField(
            model_name='sbook',
            name='sbook_issuing_authority',
            field=models.ForeignKey(default=2, blank=True, to='mariners_profile.IssuingAuthority', null=True),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='yellow_fever_issuing_authority',
            field=models.ForeignKey(default=4, blank=True, to='mariners_profile.IssuingAuthority', null=True),
        ),
    ]
