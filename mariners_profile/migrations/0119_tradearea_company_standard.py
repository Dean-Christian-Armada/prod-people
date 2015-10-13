# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0118_trainingcertificates_national_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradearea',
            name='company_standard',
            field=models.NullBooleanField(),
        ),
    ]
