# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0111_auto_20151012_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificatedocumentsdetailed',
            name='training_place_issued',
            field=models.ForeignKey(default=1, to='mariners_profile.TrainingPlaceIssued'),
        ),
    ]
