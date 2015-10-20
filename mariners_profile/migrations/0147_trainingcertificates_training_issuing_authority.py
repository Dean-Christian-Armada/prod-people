# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0146_auto_20151019_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificates',
            name='training_issuing_authority',
            field=models.ForeignKey(default=5, to='mariners_profile.IssuingAuthority'),
        ),
    ]
