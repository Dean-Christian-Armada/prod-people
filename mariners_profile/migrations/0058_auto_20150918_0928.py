# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0057_rank_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingcertificates',
            name='segregation',
        ),
        migrations.AddField(
            model_name='trainingcertificates',
            name='department',
            field=models.ForeignKey(default=6, to='mariners_profile.Departments'),
        ),
        migrations.DeleteModel(
            name='TrainingCertificatesSegregation',
        ),
    ]
