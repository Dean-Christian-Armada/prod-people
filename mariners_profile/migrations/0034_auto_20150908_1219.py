# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0033_auto_20150908_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flagdocumentsdetailed',
            name='license_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flagdocumentsdetailed',
            name='sbook_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
