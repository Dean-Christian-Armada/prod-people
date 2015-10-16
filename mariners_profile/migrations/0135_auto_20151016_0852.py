# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0134_auto_20151016_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flags',
            name='principal_standard',
        ),
        migrations.RemoveField(
            model_name='trainingcertificates',
            name='principal_standard',
        ),
        migrations.AddField(
            model_name='principal',
            name='flags_standard',
            field=models.ManyToManyField(to='mariners_profile.Flags', blank=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='training_certificate_standard',
            field=models.ManyToManyField(to='mariners_profile.TrainingCertificates', blank=True),
        ),
    ]
