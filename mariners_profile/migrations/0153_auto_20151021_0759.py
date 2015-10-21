# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0152_auto_20151020_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='flagdocumentsdetailed',
            name='flags_boolean',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainingcertificatedocumentsdetailed',
            name='trainings_certificates_boolean',
            field=models.BooleanField(default=False),
        ),
    ]
