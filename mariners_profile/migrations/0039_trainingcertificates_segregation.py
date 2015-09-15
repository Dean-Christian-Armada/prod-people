# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0038_trainingcertificatessegregation'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificates',
            name='segregation',
            field=models.ForeignKey(default=1, to='mariners_profile.TrainingCertificatesSegregation'),
        ),
    ]
