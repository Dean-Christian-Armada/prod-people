# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0156_auto_20151021_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='passport_issuing_authority',
            field=models.ForeignKey(default=3, blank=True, to='mariners_profile.IssuingAuthority', null=True),
        ),
    ]
