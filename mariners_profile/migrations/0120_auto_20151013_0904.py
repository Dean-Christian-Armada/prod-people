# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0119_tradearea_company_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcenter',
            name='company_standard',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='trainingcertificatedocumentsdetailed',
            name='place_trained',
            field=models.ForeignKey(to='mariners_profile.TrainingCenter'),
        ),
    ]
