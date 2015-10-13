# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0117_auto_20151013_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificates',
            name='national_certificate',
            field=models.BooleanField(default=False),
        ),
    ]
