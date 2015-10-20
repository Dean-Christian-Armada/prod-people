# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0142_auto_20151019_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='yellowfever',
            name='yellow_fever_issuing_authority',
            field=models.ForeignKey(default=1, to='mariners_profile.IssuingAuthority'),
        ),
    ]
