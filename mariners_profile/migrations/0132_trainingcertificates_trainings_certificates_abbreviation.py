# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0131_marinerstatushistory_mariner_status_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificates',
            name='trainings_certificates_abbreviation',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
        ),
    ]
