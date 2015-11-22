# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0195_auto_20151120_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='spouse',
            name='spouse_working',
            field=models.NullBooleanField(default=None),
        ),
    ]
