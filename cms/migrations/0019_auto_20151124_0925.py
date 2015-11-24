# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_auto_20151122_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='subfolder',
            name='high_notifier',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='subfolder',
            name='low_notifier',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='subfolder',
            name='medium_notifier',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
