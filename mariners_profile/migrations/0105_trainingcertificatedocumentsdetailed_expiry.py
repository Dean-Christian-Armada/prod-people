# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0104_auto_20151009_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcertificatedocumentsdetailed',
            name='expiry',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
