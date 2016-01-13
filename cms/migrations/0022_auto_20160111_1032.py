# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_updatefileinfolog'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatefileinfolog',
            name='new_value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='updatefileinfolog',
            name='old_value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
