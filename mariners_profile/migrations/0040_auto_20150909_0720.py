# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0039_trainingcertificates_segregation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcenter',
            name='training_center',
            field=models.CharField(default=None, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='place_trained',
            field=models.ForeignKey(to='mariners_profile.TrainingCenter'),
        ),
    ]
