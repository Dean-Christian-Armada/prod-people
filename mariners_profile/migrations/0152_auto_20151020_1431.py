# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariners_profile', '0151_seaservice_cause_of_discharge_abbreviation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seaservice',
            name='cause_of_discharge_abbreviation',
        ),
        migrations.AddField(
            model_name='causeofdischarge',
            name='cause_of_discharge_abbreviation',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
        ),
    ]
