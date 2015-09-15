# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0014_auto_20150907_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spouse',
            name='spouse_contact',
            field=models.BigIntegerField(default=None, null=True, blank=True),
        ),
    ]
