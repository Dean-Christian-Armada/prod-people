# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0103_allotee'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='branch',
            name='company_standard',
            field=models.NullBooleanField(default=True, max_length=50),
        ),
    ]
