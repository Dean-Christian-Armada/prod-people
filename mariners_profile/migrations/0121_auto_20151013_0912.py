# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0120_auto_20151013_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcenter',
            name='company_standard',
            field=models.NullBooleanField(default=True),
        ),
    ]
