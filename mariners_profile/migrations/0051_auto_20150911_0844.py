# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0050_auto_20150911_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='passport_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sbook',
            name='sbook_date_issued',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
